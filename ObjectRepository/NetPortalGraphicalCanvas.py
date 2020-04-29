from selenium.webdriver import ActionChains
import cx_Oracle
import sys


class GraphicalCanvas:

    def __init__(self, driver):
        self.driver = driver

        # Constants for all possible values of the OBJECTTYPE column in the USERGRAPHPREFERENCES table
        self.GRAPH_INSTANCE_TYPE_CLOUD = 0
        self.GRAPH_INSTANCE_TYPE_LOCATION_GROUP = 1
        self.GRAPH_INSTANCE_TYPE_LOCATION = 2
        self.GRAPH_INSTANCE_TYPE_LOGICAL_DEVICE = 3
        self.GRAPH_INSTANCE_TYPE_NETWORK_ELEMENT = 4
        self.GRAPH_INSTANCE_TYPE_VIEW_GROUP = 5
        self.GRAPH_INSTANCE_TYPE_NETWORK_GROUP = 6
        self.GRAPH_INSTANCE_TYPE_MULTIPOINT_GROUP = 7
        self.GRAPH_INSTANCE_TYPE_GENERIC_NODE = 8

        self.graphical_iframe_id = "graphIframe"
        self.canvas_id = "canvas"
        self.graph_canvas_xpath = "//div[starts-with(@id, 'graphcanvas')]"

    def right_click_node(self, db_coordinates):
        # This function performs a right-click on the code currently at the specified graph coordinates

        # Shift the graph such that the upper left hand of the graph will be coordinate (0,0)
        self.set_canvas_view_point(0, 0)

        # Shift the node to be in the upper left position of the graph
        self.move_graph_point_to_upper_left(db_coordinates[0], db_coordinates[1])

        # Click the node, which is now in the very upper left corner of the graph
        self.right_click_upper_left()

    def get_graphical_coordinates_for_network_element_in_circuit_graph(self, circuit_name, node_name):
        instance_id_sql = "select id from link where name = '" + circuit_name + "'"
        object_id_sql = "select equipmentid from networkelement where equipmentname = '" + node_name + "'"
        field_name = 'multipointCircuitLayout'
        return self.get_graphical_coordinates(field_name, instance_id_sql, self.GRAPH_INSTANCE_TYPE_NETWORK_ELEMENT,
                                              object_id_sql)

    def get_graphical_coordinates(self, field_name, instance_id_sql, object_type, object_id_sql):
        # This function is meant to be used to get the coordinates for a node in any graph display

        # Connect to the DB
        # TODO: made this configurable
        con = cx_Oracle.connect('QC253/qc253@192.168.221.184:1521/pdborcl')
        # dsn_str = cx_Oracle.makedsn("192.168.223.234", "1522", "orcl")
        # con = cx_Oracle.connect(user="TNP_DEV_EB_TVDEV", password="TNP_DEV_EB_TVDEV", dsn=dsn_str)

        cursor = con.cursor()

        sql_query = ("select xcoordinate, ycoordinate from usergraphpreferences where instanceid = ("
                     + instance_id_sql + ") and fieldname = '" + field_name + "' and objecttype = "
                     + str(object_type) + " and objectid = (" + object_id_sql + ")")

        print(sql_query)
        cursor.execute(sql_query)

        # Only one result row. row contains an array of x and y coordinate
        row = cursor.fetchone()

        cursor.close()
        con.close()

        if row is None:
            sys.exit("No coordinates are found in the database.")

        return row

    def get_total_offset_factor(self):
        # Determine the factor that must be multiplied against offsets to be moved. This correlates
        # the coordinates stored in the DB to actual offsets to move the mouse to reach the node.
        # Currently, the zoom factor does not seem to be enough, and it requires an additional factor of 2

        factor = 2
        zoom_factor = self.get_current_zoom()
        total_factor = factor * zoom_factor
        return total_factor

    def get_graphical_iframe(self):
        element = self.driver.find_element_by_id(self.graphical_iframe_id)
        return element

    def switch_to_graph_iframe(self):
        self.driver.switch_to.frame(self.graphical_iframe_id)

    def get_graph_canvas(self):
        element = self.driver.find_element_by_id(self.canvas_id)
        return element

    def move_graph_point_to_upper_left(self, x, y):
        graph_canvas = self.get_graph_canvas()
        action_chains = ActionChains(self.driver)

        x_is_neg = True if x < 0 else False
        y_is_neg = True if y < 0 else False

        # Need to multiple the offsets to move by the current zoom factor of the graph.
        # Also multiple by negative 1 because need to move in the opposite direction
        total_factor = self.get_total_offset_factor()
        offset_x_to_drag = x * -1 * total_factor
        offset_y_to_drag = y * -1 * total_factor

        # Determine the height and width of the canvas
        graph_canvas_size = graph_canvas.size
        graph_canvas_half_height = graph_canvas_size["height"] / 2
        graph_canvas_half_width = graph_canvas_size["width"] / 2
        print("graph_canvas_half_width: " + str(graph_canvas_half_width))
        print("graph_canvas_half_height: " + str(graph_canvas_half_height))

        # Click in the CENTER of the graph canvas and then pan in just the horizontal direction, in order to bring the
        # node to the left side of the graph. If the x offset is larger than half the width of the canvas, then need
        # to break up the distance into several drag and drops, so as not to end the drag off the canvas (which would
        # not move the graph and would leave the graph in panning mode)
        while True:
            if x == 0:
                break
            if x_is_neg:
                value_to_move = min(offset_x_to_drag, graph_canvas_half_width - 5)
            else:
                value_to_move = max(offset_x_to_drag, (graph_canvas_half_width - 5) * -1)

            print("Moving horizontally by offset: " + str(offset_x_to_drag))
            action_chains.move_to_element(graph_canvas).click_and_hold().move_by_offset(value_to_move, 0) \
                .release().perform()

            offset_x_to_drag = offset_x_to_drag - value_to_move

            if offset_x_to_drag == 0:
                break

            # Seem to need a new instance of ActionChains, otherwise it moves too far
            action_chains = ActionChains(self.driver)

        # Click in the CENTER of the graph canvas and then pan in just the vertical direction, in order to bring the
        # node to the upper left corner of the graph. If the y offset is larger than half the height of the canvas, then
        # need to break up the distance into several drag and drops, so as not to end the drag off the canvas (which
        # would not move the graph and would leave the graph in panning mode)
        while True:
            if y == 0:
                break
            if y_is_neg:
                value_to_move = min(offset_y_to_drag, graph_canvas_half_height - 5)
            else:
                value_to_move = max(offset_y_to_drag, (graph_canvas_half_height - 5) * -1)

            print("Moving vertically by offset: " + str(offset_y_to_drag))
            action_chains.move_to_element(graph_canvas).click_and_hold().move_by_offset(0, value_to_move) \
                .release().perform()

            offset_y_to_drag = offset_y_to_drag - value_to_move

            if offset_y_to_drag == 0:
                break

            # Seem to need a new instance of ActionChains, otherwise it moves too far
            action_chains = ActionChains(self.driver)

    def right_click_upper_left(self):
        # Get the graph canvas
        graph_canvas = self.driver.find_element_by_id(self.canvas_id)
        action_chains = ActionChains(self.driver)

        # Determine the x and y offsets required to move from the CENTER of the canvas to the upper left of the canvas
        graph_canvas_size = graph_canvas.size
        graph_canvas_height = graph_canvas_size["height"]
        graph_canvas_width = graph_canvas_size["width"]
        offset_x = (graph_canvas_width / 2) * -1
        offset_y = (graph_canvas_height / 2) * -1

        # Determine x and y offsets required to move from the upper left of a node to the approximate center
        # of a node, assuming default node size. Need to multiple by zoom factor
        # TODO: Handle nodes of various sizes and group nodes?
        half_default_node_size = 20
        offset_to_node_center = half_default_node_size * self.get_current_zoom()

        # Move the mouse to the center of the graph canvas, then move the mouse to the upper left corner of the
        # graph canvas (and move in a bit more to the right and down to aim for more center of the node) and
        # perform a right-click
        action_chains.move_to_element(graph_canvas).move_by_offset(offset_x, offset_y) \
            .move_by_offset(offset_to_node_center, offset_to_node_center).context_click().perform()

    def get_current_zoom(self):
        # This function calls javascript running inside the application to retrieve the real zoom factor currently
        # set on the graph canvas

        # Get the element with ID that starts with "graphcanvas"
        graph_canvas = self.driver.find_element_by_xpath(self.graph_canvas_xpath)

        # Now get the full ID, which is in the format: graphcanvas_<ui_id>_<fieldName>
        # We need these two variables to be able to find the yfiles GraphObj
        graph_canvas_id = graph_canvas.get_attribute("id")
        arr = graph_canvas_id.split("_")
        ui_id = arr[1]
        field_name = arr[2]

        # Must switch back to the parent (top) because that is where the javascript function resides
        self.driver.switch_to.parent_frame()

        # Execute javascript to get the yfiles GraphObj and then call function to get the current zoom factor
        current_zoom = self.driver.execute_script("""
            var graph_handle = window.getYFilesGraph(arguments[0]);
            if (graph_handle) {
                return graph_handle.graph._getCurrentZoom()
            }
            return -1;
            """, ui_id + "-" + field_name)

        # Return context back to the iframe
        self.switch_to_graph_iframe()

        return current_zoom

    def set_canvas_view_point(self, x, y):
        # Get the element with ID that starts with "graphcanvas"
        graph_canvas = self.driver.find_element_by_xpath(self.graph_canvas_xpath)

        # Now get the full ID, which is in the format: graphcanvas_<ui_id>_<fieldName>
        # We need these two variables to be able to find the yfiles GraphObj
        graph_canvas_id = graph_canvas.get_attribute("id")
        arr = graph_canvas_id.split("_")
        ui_id = arr[1]
        field_name = arr[2]

        # Must switch back to the parent (top) because that is where the javascript function resides
        self.driver.switch_to.parent_frame()

        # Execute javascript to get the yfiles GraphObj and then call function to get the current zoom factor
        self.driver.execute_script("""
            var graph_handle = window.getYFilesGraph(arguments[0]);
            if (graph_handle) {
                graph_handle.graph._setCanvasViewPoint(arguments[1],arguments[2]);
            }
            """, ui_id + "-" + field_name, x, y)

        # Return context back to the iframe
        self.switch_to_graph_iframe()

    def click_lower_right(self):
        # This function was just a helper function in testing, to click on empty canvas in the lower right

        # Get the graph canvas
        graph_canvas = self.driver.find_element_by_id(self.canvas_id)
        action_chains = ActionChains(self.driver)

        # Determine the x and y offsets required to move from the CENTER of the canvas to just inside the lower right
        # of the canvas
        graph_canvas_size = graph_canvas.size
        graph_canvas_height = graph_canvas_size["height"]
        graph_canvas_width = graph_canvas_size["width"]
        offset_x = (graph_canvas_width / 2) - 5
        offset_y = (graph_canvas_height / 2) - 5

        # Move the mouse to the center of the graph canvas, then move the mouse to the lower left corner of the
        # graph canvas and perform a click operation (ie: to clear any displayed context menu)
        action_chains.move_to_element(graph_canvas).move_by_offset(offset_x, offset_y).click().perform()
