import time
from ObjectRepository.NetportalHomePage import HomePage
from ObjectRepository.NetportalL1RFS_Page import L1RFSPage
from ObjectRepository.NetportalCircuitPage import Circuit
from ObjectRepository.NetPortalGraphicalCanvas import GraphicalCanvas

class TestCircuit:
################################################### DATA INPUT #########################################################
    ### NE-TYPE INSTALLATION DATA ###
    NEtypeName="alcatel.1678"

    ### NETWORK ELEMENTS DATA ###
    NETypeName1="Alcatel 1678"
    NEName1="Alcatel-018"
    NEName2="Alcatel-027"
    OperationalStatusIM="Installed / Maintenance"
    OperationalStatusIS="In Service"
    ShelfType="Alcatel 1678 MCC Main Shelf"
    CurrentOperationalStatus1="Planned"
    NewOperationalStatusIM = "Installed / Maintenance"
    NewOperationalStatusIS = "In Service"

    ### FACILITY DATA ###
    FacilityName="FAC-011-025"
    LayerRate="Gigabit Ethernet"

########################################################################################################################
    def __init__(self, driver):
        self.driver = driver

    def TCP_AUT_GUI_INV_MIV_L1S_LAYER1_001_00005_POS_Test(self):
        #Circuit
        a = HomePage(self.driver)

        a.click_Connectivity()
        time.sleep(2)
        a.click_L1RFS()
        time.sleep(3)

        L1RFS = L1RFSPage(self.driver)
        L1RFS.click_Create()
        time.sleep(3)
        L1RFS.click_Circuit()
        time.sleep(3)

        circuit = Circuit(self.driver)
        circuit.select_CircuitLayerRate()
        time.sleep(2)
        circuit.click_SearchIconSourceNode()
        time.sleep(2)
        circuit.enter_SourceNEName(self.NEName1)
        time.sleep(2)
        circuit.click_SearchSourceNEName()
        time.sleep(2)
        circuit.click_SelectSourceNEName()
        time.sleep(10)
        circuit.click_SearchIconTargetNode()
        time.sleep(4)
        circuit.enter_TargetNEName(self.NEName2)
        time.sleep(3)
        circuit.click_SearchTargetNEName()
        time.sleep(14)
        circuit.click_SelectTargetNEName()
        time.sleep(5)
        circuit.click_SaveIcon()
        circuit_name = circuit.get_circuit_name()
        circuit.click_CiruitLayout()
        time.sleep(5)

        canvas = GraphicalCanvas(self.driver)
        canvas.switch_to_graph_iframe()

        # Right-click on A-END
        print("Right-click on " + self.NEName1)
        ne_coords = canvas.get_graphical_coordinates_for_network_element_in_circuit_graph(circuit_name, self.NEName1)
        canvas.right_click_node(ne_coords)

        time.sleep(3)

        # Clear the right-click menu
        canvas.click_lower_right()

        # Right-click on Z-END
        print("Right-click on " + self.NEName2)
        ne_coords = canvas.get_graphical_coordinates_for_network_element_in_circuit_graph(circuit_name, self.NEName2)
        canvas.right_click_node(ne_coords)

        time.sleep(5)

        # circuit.click_AddSegmentMenu()


















