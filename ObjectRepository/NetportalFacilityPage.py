from selenium.webdriver.support.select import Select


class Facility:

    def __init__(self,driver):
        self.driver =driver

        self.facilityName_id="gwt-debug-textbox-field-generic.namefacility.facility.details"
        self.layerRate_id="gwt-debug-dropdown-field-link.layerratefacility.facility.details"
        self.searchSourceNEIcon_id="gwt-debug-lookup-search-field-link.aEndNodeIdfacility.facility.details"
        self.sourceNEName_xpath="/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td/input"
        self.searchSourceNE_xpath="/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/input"
        self.selectSourceNE_xpath="/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[2]/td[3]/a"
        self.targetNEName_xpath="/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td/input"
        self.searchTargetNE_xpath="/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/input"
        self.selectTargetNE_xpath="/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[2]/td[3]/a"
        self.sourcePort_xpath="/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[2]/td[4]/a"
        self.targetPort_xpath="/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[2]/td[4]/a"
        self.saveFacility_id="gwt-debug-toolbar-icon-savefacilityChannel.facilityChannel.search.result"
        self.closeFacility_id="gwt-debug-toolbar-icon-closelink.connection.link.connection.result"
        self.actionMenu_xpath="/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/div"
        self.virtualEnable_id="gwt-debug-custom-dropdown-item-facility.virtualEnablelink.connection.link.connection.result"





    def enter_FacilityName(self,facilityName):
        self.driver.find_element_by_id(self.facilityName_id).send_keys(facilityName)

    def select_LayerRate(self, visibleText):
        element = self.driver.find_element_by_id(self.layerRate_id)
        drop = Select(element)
        drop.select_by_visible_text(visibleText)

    def  click_SearchSourceNEIcon(self):
        self.driver.find_element_by_id(self.searchSourceNEIcon_id).click()

    def enter_SourceNEName(self,sourceNE):
        self.driver.find_element_by_xpath(self.sourceNEName_xpath).send_keys(sourceNE)

    def click_SearchSourceNE(self):
        self.driver.find_element_by_xpath(self.searchSourceNE_xpath).click()

    def click_SelectSourceNE(self):
        self.driver.find_element_by_xpath(self.selectSourceNE_xpath).click()

    def enter_TargetNEName(self,targetNE):
        self.driver.find_element_by_xpath(self.targetNEName_xpath).send_keys(targetNE)

    def click_SearchTargetNE(self):
        self.driver.find_element_by_xpath(self.searchTargetNE_xpath).click()

    def click_SelectTargetNE(self):
        self.driver.find_element_by_xpath(self.selectTargetNE_xpath).click()

    def click_SourcePort(self):
        self.driver.find_element_by_xpath(self.sourcePort_xpath).click()

    def click_TargetPort(self):
        self.driver.find_element_by_xpath(self.targetPort_xpath).click()

    def click_SaveFacility(self):
        self.driver.find_element_by_id(self.saveFacility_id).click()

    def click_CloseFacility(self):
        self.driver.find_element_by_id(self.closeFacility_id).click()

    def click_ActionMenu(self):
        self.driver.find_element_by_xpath(self.actionMenu_xpath).click()

    def click_VirtualEnable(self):
        self.driver.find_element_by_id(self.virtualEnable_id).click()