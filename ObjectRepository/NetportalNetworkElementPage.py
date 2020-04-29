from lib2to3.pgen2 import driver
from selenium.webdriver.support.select import Select


class NetworkElementPage:

    def __init__(self, driver):
        self.driver = driver

        self.NECreate_id = "gwt-debug-button-menu-networkElement.addnetworkElement.networkElement.search"
        self.NEType_id = "gwt-debug-textbox-field-neInstalledAdapter.productneInstalledAdapter.neInstalledAdapter.search"
        self.searchNeType_id = "gwt-debug-Button-SearchneInstalledAdapter.neInstalledAdapter.search"
        self.selectNEType_xpath = "/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[2]/td[3]/a"
        self.NEName_id = "gwt-debug-textbox-field-ne.equipmentNamenetworkElement.networkElement.details.modified"
        self.SaveNE_id = "gwt-debug-toolbar-icon-savelogical.device.device.details"
        self.oeprationalStatus_id = "gwt-debug-dropdown-field-ne.operationalStatenetworkElement.networkElement.details.modified"
        self.physicalConfigurationTab_id = "gwt-debug-TabBar-1networkElement.networkElement.details.modified-tab3"
        self.textualTab_id = "gwt-debug-TabBar-1networkElement.networkElement.details.modified-tab1"
        self.addShelf_id = "gwt-debug-form-button-addShelfphysicalConfig.rackConfig.textual.formField"
        self.shelfType_id = "gwt-debug-dropdown-field-defineEquipmentHolder.typedefineEquipmentHolder.defineShelves"
        self.okShelfType_id = "gwt-debug-form-button-addShelvesdefineEquipmentHolder.defineShelves"
        self.okShelfCreated_id = "gwt-debug-Button-OKdefineEquipmentHolder.defineShelves"
        self.shelfLabel_xpath = "(//*[@id='c_0_1']/img)[2]"
        self.shelfDetails_id = "gwt-debug-form-button-showShelfDetailsphysicalConfig.rackConfig.textual.formField"
        self.equipmentAddress1_xpath = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td/div/div/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[3]/td[2]/img"
        self.equipmentAddress2_xpath = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td/div/div/div/div[4]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td/div/div[2]/table/tbody/tr/td/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[4]/td[2]/img"
        self.selectCard_id = "gwt-debug-form-button-selectCardTextualphysicalConfig.shelfConfig.textual.formField"
        self.cardLabel_xpath = "/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[7]/td[3]/a"
        self.cardLabel2_xpath = "/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[6]/td[3]/a"
        self.cardLabel2_1_xpath = "/html/body/div[5]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[2]/td[3]/a"
        self.actionMenu_id = "gwt-debug-action-dropdown-networkElement.addToProjectphysicalConfig.rackConfig.result"
        self.cardOperationalStatus_id = "gwt-debug-custom-dropdown-item-networkElement.bulkChangeCardOperationalStatusphysicalConfig.rackConfig.result"
        self.currentOperationalStatus_id = "gwt-debug-dropdown-field-operationalState.currentbulkChangeCardOperationalStatus.detail"
        self.searchCurrentOperationalStatus_id = "gwt-debug-form-button-searchbulkChangeCardOperationalStatus.detail"
        self.allCurrentOperationalStatus_xpath = "/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr[2]/td[2]/div/img"
        self.newOperationalStatus_id = "gwt-debug-dropdown-field-operationalState.newbulkChangeCardOperationalStatus.detail"
        self.clickOk_id = "gwt-debug-form-button-okbulkChangeCardOperationalStatus.detail"
        self.closeNE_xpath = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table/tbody/tr/td/table/tbody/tr/td[5]/table/tbody/tr/td/div"
        self.NENameText_xpath = "//div[contains(text(),'Network Element: Alcatel-013')]"

    def click_NECreate(self):
        self.driver.find_element_by_id(self.NECreate_id).click()

    def enter_NEType(self, NEtypeName):
        self.driver.find_element_by_id(self.NEType_id).send_keys(NEtypeName)

    def click_SearchNEType(self):
        self.driver.find_element_by_id(self.searchNeType_id).click()

    def click_SelectNEType(self):
        self.driver.find_element_by_xpath(self.selectNEType_xpath).click()

    def enter_NEName(self, NEName):
        self.driver.find_element_by_id(self.NEName_id).send_keys(NEName)

    def assert_NEName(self):
        self.driver.find_element_by_id(self.NEName_id)

    def click_SaveNE(self):
        self.driver.find_element_by_id(self.SaveNE_id).click()

    def get_NENameText(self):
        self.driver.find_element_by_xpath(self.NENameText_xpath).text

    def select_OperationalStatus(self, visibleText):
        element = self.driver.find_element_by_id(self.oeprationalStatus_id)
        drop = Select(element)
        drop.select_by_visible_text(visibleText)

    def click_PhysicalConfigurationTab(self):
        self.driver.find_element_by_id(self.physicalConfigurationTab_id).click()

    def click_TextualTab(self):
        self.driver.find_element_by_id(self.textualTab_id).click()

    def click_AddShelf(self):
        self.driver.find_element_by_id(self.addShelf_id).click()

    def select_ShelfType(self, visibleText):
        element = self.driver.find_element_by_id(self.shelfType_id)
        drop = Select(element)
        drop.select_by_visible_text(visibleText)

    def click_OkShelfType(self):
        self.driver.find_element_by_id(self.okShelfType_id).click()

    def click_OkShelfCreated(self):
        self.driver.find_element_by_id(self.okShelfCreated_id).click()

    def click_ShelfLabel(self):
        self.driver.find_element_by_xpath(self.shelfLabel_xpath).click()

    def click_ShelfDetails(self):
        self.driver.find_element_by_id(self.shelfDetails_id).click()

    def click_EquipmentAddress1(self):
        self.driver.find_element_by_xpath(self.equipmentAddress1_xpath).click()

    def click_EquipmentAddress2(self):
        self.driver.find_element_by_xpath(self.equipmentAddress2_xpath).click()

    def click_SelectCard(self):
        self.driver.find_element_by_id(self.selectCard_id).click()

    def click_cardLabel(self):
        self.driver.find_element_by_xpath(self.cardLabel_xpath).click()

    def click_cardLabel2(self):
        self.driver.find_element_by_xpath(self.cardLabel2_xpath).click()

    def click_cardLabel2_1(self):
        self.driver.find_element_by_xpath(self.cardLabel2_1_xpath).click()

    def click_ActionMenu(self):
        self.driver.find_element_by_id(self.actionMenu_id).click()

    def click_CardOperationalStatus(self):
        self.driver.find_element_by_id(self.cardOperationalStatus_id).click()

    def select_CurrentOperationalStatus(self, visibleText):
        element = self.driver.find_element_by_id(self.currentOperationalStatus_id)
        drop = Select(element)
        drop.select_by_visible_text(visibleText)

    def click_SearchCurrentOperationalStatus(self):
        self.driver.find_element_by_id(self.searchCurrentOperationalStatus_id).click()

    def click_AllCurrentOperationalStatus(self):
        self.driver.find_element_by_xpath(self.allCurrentOperationalStatus_xpath).click()

    def select_NewOperationalStatus(self, visibleText):
        element = self.driver.find_element_by_id(self.newOperationalStatus_id)
        drop = Select(element)
        drop.select_by_visible_text(visibleText)

    def click_OK(self):
        self.driver.find_element_by_id(self.clickOk_id).click()

    def click_CloseNE(self):
        self.driver.find_element_by_xpath(self.closeNE_xpath).click()

    def click_CloseBrowser(self):
        self.driver.close()
