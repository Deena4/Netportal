class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.admin_id = "gwt-debug-submenuitem-admin"
        self.cmdb_id = "gwt-debug-submenuitem-adminCmdb"
        self.NETypes_id = "gwt-debug-submenuitem-netype.config"
        self.Install_id = "gwt-debug-button-menu-adapter.installneInstalledAdapter.neInstalledAdapter.master.search"
        self.adapterName_id = "gwt-debug-textbox-field-instAdapter.nameneInstalledAdapter.installedAdapter.search"
        self.adapterSearch_id = "gwt-debug-Button-SearchneInstalledAdapter.installedAdapter.search"
        self.adapterSelectall_xpath = "/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr[2]/td[2]/div/img"
        self.adapterSelect_id = "gwt-debug-button-menu-installedAdapter.menu.selectneInstalledAdapter.installedAdapter.search"
        self.Ok_id = "gwt-debug-Button-OKneInstalledAdapter.installedAdapter.result"
        self.Resources_id = "gwt-debug-submenuitem-resources"
        self.Networkelement_id = "gwt-debug-submenuitem-networkElements"
        self.Connectivity_id = "gwt-debug-submenuitem-connectivity"
        self.L1RFS_id = "gwt-debug-submenuitem-layer1.links"
        self.clickCustomers_id = "gwt-debug-submenuitem-customers"
        self.Provider_id = "gwt-debug-submenuitem-providers"
        self.Location_id = "gwt-debug-submenuitem-locations"
        self.Dashboard_id = "gwt-debug-submenuitem-dashboard"
        self.View_id = "gwt-debug-submenuitem-views"

    def click_admin(self):
        self.driver.find_element_by_id(self.admin_id).click()

    def click_cmdb(self):
        self.driver.find_element_by_id(self.cmdb_id).click()

    def click_NETypes(self):
        self.driver.find_element_by_id(self.NETypes_id).click()

    def click_Install(self):
        self.driver.find_element_by_id(self.Install_id).click()

    def enter_adapterName(self, NEtypeName):
        self.driver.find_element_by_id(self.adapterName_id).send_keys(NEtypeName)

    def click_adapterSearch(self):
        self.driver.find_element_by_id(self.adapterSearch_id).click()

    def click_adapterSelectall(self):
        self.driver.find_element_by_xpath(self.adapterSelectall_xpath).click()

    def click_adapterSelect(self):
        self.driver.find_element_by_id(self.adapterSelect_id).click()

    def click_Ok(self):
        self.driver.find_element_by_id(self.Ok_id).click()

    def click_Resources(self):
        self.driver.find_element_by_id(self.Resources_id).click()

    def click_Networkelement(self):
        self.driver.find_element_by_id(self.Networkelement_id).click()

    def click_Connectivity(self):
        self.driver.find_element_by_id(self.Connectivity_id).click()

    def click_L1RFS(self):
        self.driver.find_element_by_id(self.L1RFS_id).click()

    def click_Customers(self):
        self.driver.find_element_by_id(self.clickCustomers_id).click()

    def click_Provider(self):
        self.driver.find_element_by_id(self.Provider_id).click()

    def click_Location(self):
        self.driver.find_element_by_id(self.Location_id).click()

    def click_Dashboard(self):
        self.driver.find_element_by_id(self.Dashboard_id).click()

    def click_view(self):
        self.driver.find_element_by_id(self.View_id).click()
