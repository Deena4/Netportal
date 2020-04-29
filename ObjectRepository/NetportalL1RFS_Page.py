class L1RFSPage:

    def __init__(self,driver):
        self.driver =driver

        self.create_id="gwt-debug-button-menu-connectivity.addlink.layer1.links.search"
        self.facility_xpath="/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[2]/td[3]/a"
        self.circuit_xpath = "/html/body/div[4]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[3]/td[3]/a"

    def click_Create(self):
        self.driver.find_element_by_id(self.create_id).click()

    def click_Facility(self):
        self.driver.find_element_by_xpath(self.facility_xpath).click()

    def click_Circuit(self):
        self.driver.find_element_by_xpath(self.circuit_xpath).click()