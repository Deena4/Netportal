from selenium.webdriver.support.select import Select
import time


class Circuit:

    def __init__(self, driver):
        self.driver = driver

        self.circuitName_id = "gwt-debug-textbox-field-generic.namepath.path.details"
        self.circuitLayerRate_id = "gwt-debug-dropdown-field-link.layerratepath.path.details"
        self.searchIconSourceNode_id = "gwt-debug-lookup-search-field-link.aEndNodeIdpath.path.details"
        self.sourceNEName_id = "gwt-debug-textbox-field-ne.equipmentNamenetworkElement.networkElement.search"
        self.searchSourceNEName_id = "gwt-debug-Button-SearchnetworkElement.networkElement.search"
        self.selectSourceNEName_xpath = "/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[2]/td[3]/a"
        self.searchIconTargetNode_id = "gwt-debug-lookup-search-field-link.zEndNodeIdpath.path.details"
        self.targetNEName_id = "gwt-debug-textbox-field-ne.equipmentNamenetworkElement.networkElement.search"
        self.searchTargetNEName_id = "gwt-debug-Button-SearchnetworkElement.networkElement.search"
        self.selectTargetNEName_xpath = "/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[2]/td[3]/a"
        self.circuitLayout_id = "gwt-debug-TabBar-1path.path.details-tab1"
        self.rightClick_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[3]/img"
        self.adjustChannels_xpath = "//td[contains(text(),'Adjust Channels')]"
        self.rightClickNE_xpath = "//div[@class='yFilesGraphCanvasOverlay']"
        self.save_id = "gwt-debug-action-icon-.savedocument.object.link.documentManagement.widget.form.linkedDocuments"
        self.addSegmentMenu_id = "dijit_MenuItem_8_text"

    def enter_circuitName(self, circuitName):
        self.driver.find_element_by_id(self.circuitName_id).send_keys(circuitName)

    def select_CircuitLayerRate(self):
        element = self.driver.find_element_by_id(self.circuitLayerRate_id)
        drop = Select(element)
        drop.select_by_value('155')

    def click_SearchIconSourceNode(self):
        self.driver.find_element_by_id(self.searchIconSourceNode_id).click()

    def enter_SourceNEName(self, sourceNE):
        self.driver.find_element_by_id(self.sourceNEName_id).send_keys(sourceNE)

    def click_SearchSourceNEName(self):
        self.driver.find_element_by_id(self.searchSourceNEName_id).click()

    def click_SelectSourceNEName(self):
        self.driver.find_element_by_xpath(self.selectSourceNEName_xpath).click()

    def click_SearchIconTargetNode(self):
        self.driver.find_element_by_id(self.searchIconTargetNode_id).click()

    def enter_TargetNEName(self, TargetNE):
        self.driver.find_element_by_id(self.targetNEName_id).send_keys(TargetNE)

    def click_SearchTargetNEName(self):
        self.driver.find_element_by_id(self.searchTargetNEName_id).click()

    def click_SelectTargetNEName(self):
        self.driver.find_element_by_xpath(self.selectTargetNEName_xpath).click()

    def click_CiruitLayout(self):
        self.driver.find_element_by_id(self.circuitLayout_id).click()

    def click_AddSegmentMenu(self):
        self.driver.find_element_by_id(self.addSegmentMenu_id).click()

    def click_AdjustChannels(self):
        self.driver.find_element_by_xpath(self.adjustChannels_xpath).click()

    def click_SaveIcon(self):
        self.driver.find_element_by_id(self.save_id).click()

    def get_circuit_name(self):
        element = self.driver.find_element_by_id(self.circuitName_id)
        value = element.get_attribute("value")

        # If the value has not yet been set in the name field yet, loop until it is present
        if value is None or not value.strip():
            while True:
                time.sleep(1)
                value = element.get_attribute("value")
                if value is not None and value.strip():
                    break
        print("Circuit Name: " + value.strip())
        return value
