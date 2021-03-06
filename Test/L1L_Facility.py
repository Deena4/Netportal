import time

from ObjectRepository.NetportalHomePage import HomePage
from ObjectRepository.NetportalNetworkElementPage import NetworkElementPage
from ObjectRepository.NetportalL1RFS_Page import L1RFSPage
from ObjectRepository.NetportalFacilityPage import Facility


class TestFacility:
    ################################################### DATA INPUT ########################################################
    ### NE-TYPE INSTALLATION DATA ###
    NEtypeName = "alcatel.1678"

    ### NETWORK ELEMENTS DATA ###
    NETypeName1 = "Alcatel 1678"
    NEName1 = "Alcatel-018"
    NEName2 = "Alcatel-027"
    OperationalStatusIM = "Installed / Maintenance"
    OperationalStatusIS = "In Service"
    ShelfType = "Alcatel 1678 MCC Main Shelf"
    CurrentOperationalStatus1 = "Planned"
    NewOperationalStatusIM = "Installed / Maintenance"
    NewOperationalStatusIS = "In Service"

    ### FACILITY DATA ###
    FacilityName = "FAC-011-025"
    LayerRate = "Gigabit Ethernet"

    ########################################################################################################################

    def __init__(self, driver):
        self.driver = driver

    def TCP_AUT_GUI_INV_MIV_L1L_LAYER1_001_00004_POS_Test(self):
        # # #InstallNetypes
        a = HomePage(self.driver)
        time.sleep(1)
        a.click_admin()
        time.sleep(5)
        a.click_cmdb()
        time.sleep(2)
        a.click_NETypes()
        time.sleep(2)
        a.click_Install()
        time.sleep(2)
        a.enter_adapterName(self.NEtypeName)
        time.sleep(1)
        a.click_adapterSearch()
        time.sleep(4)
        a.click_adapterSelectall()
        time.sleep(3)
        a.click_adapterSelect()
        time.sleep(1)
        a.click_Ok()

    # Create Network Element [NE-1]

        a.click_Resources()
        time.sleep(1)
        a.click_Networkelement()
        time.sleep(1)
        b = NetworkElementPage(self.driver)
        time.sleep(1)
        b.click_NECreate()
        time.sleep(1)
        b.enter_NEType(self.NETypeName1)
        time.sleep(1)
        b.click_SearchNEType()
        time.sleep(1)
        b.click_SelectNEType()
        time.sleep(2)
        b.enter_NEName(self.NEName1)
        time.sleep(3)
        b.select_OperationalStatus(self.OperationalStatusIM)
        time.sleep(5)
        b.select_OperationalStatus(self.OperationalStatusIS)
        time.sleep(8)
        b.click_SaveNE()
        time.sleep(6)
        # assert self.driver.find_element_by_xpath("//div[contains(text(),'Alcatel-006n')]").text == 'Network Element: Alcatel-006n'
        b.click_PhysicalConfigurationTab()
        time.sleep(3)
        b.click_TextualTab()
        time.sleep(3)
        b.click_AddShelf()
        time.sleep(4)
        b.select_ShelfType(self.ShelfType)
        time.sleep(3)
        b.click_OkShelfType()
        time.sleep(3)
        b.click_OkShelfCreated()
        time.sleep(3)
        b.click_ShelfLabel()
        time.sleep(3)
        b.click_ShelfDetails()
        time.sleep(5)
        b.click_EquipmentAddress2()
        time.sleep(3)
        b.click_SelectCard()
        time.sleep(3)
        b.click_cardLabel2()
        time.sleep(3)
        b.click_cardLabel2_1()
        time.sleep(4)
        b.click_EquipmentAddress1()
        time.sleep(4)
        b.click_SelectCard()
        time.sleep(3)
        b.click_cardLabel()
        time.sleep(4)
        b.click_ActionMenu()
        time.sleep(3)
        b.click_CardOperationalStatus()
        time.sleep(3)
        b.select_CurrentOperationalStatus(self.CurrentOperationalStatus1)
        time.sleep(3)
        b.click_SearchCurrentOperationalStatus()
        time.sleep(3)
        b.click_AllCurrentOperationalStatus()
        time.sleep(3)
        b.select_NewOperationalStatus(self.NewOperationalStatusIM)
        time.sleep(3)
        b.select_NewOperationalStatus(self.NewOperationalStatusIS)
        time.sleep(3)
        b.click_OK()
        time.sleep(3)
        b.click_SaveNE()
        time.sleep(5)
        b.click_CloseNE()
        time.sleep(3)

    # Create Network Element [NE-2]

        b.click_NECreate()
        time.sleep(2)
        b.enter_NEType(self.NETypeName1)
        time.sleep(1)
        b.click_SearchNEType()
        time.sleep(1)
        b.click_SelectNEType()
        time.sleep(2)
        b.enter_NEName(self.NEName2)
        time.sleep(4)
        b.select_OperationalStatus(self.OperationalStatusIM)
        time.sleep(4)
        b.select_OperationalStatus(self.OperationalStatusIS)
        time.sleep(4)
        b.click_SaveNE()
        time.sleep(5)
        # assert self.driver.find_element_by_xpath("//div[contains(text(),'Alcatel-015k')]").text == 'Network Element: Alcatel-015j'
        time.sleep(2)
        b.click_PhysicalConfigurationTab()
        time.sleep(3)
        b.click_TextualTab()
        time.sleep(3)
        b.click_AddShelf()
        time.sleep(3)
        b.select_ShelfType(self.ShelfType)
        time.sleep(3)
        b.click_OkShelfType()
        time.sleep(3)
        b.click_OkShelfCreated()
        time.sleep(3)
        b.click_ShelfLabel()
        time.sleep(3)
        b.click_ShelfDetails()
        time.sleep(4)
        b.click_EquipmentAddress2()
        time.sleep(4)
        b.click_SelectCard()
        time.sleep(3)
        b.click_cardLabel2()
        time.sleep(3)
        b.click_cardLabel2_1()
        time.sleep(4)
        b.click_EquipmentAddress1()
        time.sleep(4)
        b.click_SelectCard()
        time.sleep(3)
        b.click_cardLabel()
        time.sleep(3)
        b.click_ActionMenu()
        time.sleep(3)
        b.click_CardOperationalStatus()
        time.sleep(3)
        b.select_CurrentOperationalStatus(self.CurrentOperationalStatus1)
        time.sleep(3)
        b.click_SearchCurrentOperationalStatus()
        time.sleep(3)
        b.click_AllCurrentOperationalStatus()
        time.sleep(3)
        b.select_NewOperationalStatus(self.NewOperationalStatusIM)
        time.sleep(3)
        b.select_NewOperationalStatus(self.NewOperationalStatusIS)
        time.sleep(3)
        b.click_OK()
        time.sleep(3)
        b.click_SaveNE()
        time.sleep(5)
        b.click_CloseNE()
        time.sleep(3)

    # Create Facility [GIGE FACILITY]

        a.click_Connectivity()
        time.sleep(3)
        a.click_L1RFS()
        time.sleep(3)

        L1RFS = L1RFSPage(self.driver)
        L1RFS.click_Create()
        time.sleep(3)
        L1RFS.click_Facility()
        time.sleep(3)

        facility = Facility(self.driver)
        time.sleep(2)
        facility.enter_FacilityName(self.FacilityName)
        time.sleep(3)
        facility.select_LayerRate(self.LayerRate)
        time.sleep(4)
        facility.click_SearchSourceNEIcon()
        time.sleep(3)
        facility.enter_SourceNEName(self.NEName1)
        time.sleep(3)
        facility.click_SearchSourceNE()
        time.sleep(3)
        facility.click_SelectSourceNE()
        time.sleep(3)
        facility.enter_TargetNEName(self.NEName2)
        time.sleep(3)
        facility.click_SearchTargetNE()
        time.sleep(3)
        facility.click_SelectTargetNE()
        time.sleep(3)
        facility.click_SourcePort()
        time.sleep(2)
        facility.click_TargetPort()
        time.sleep(4)
        facility.click_SaveFacility()
        time.sleep(3)
        facility.click_ActionMenu()
        time.sleep(4)
        facility.click_VirtualEnable()
        time.sleep(2)
        facility.click_SaveFacility()
        time.sleep(3)
        facility.click_CloseFacility()
        time.sleep(2)
