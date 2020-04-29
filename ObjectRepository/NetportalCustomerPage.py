class CustomerPage:

    def __init__(self, driver):
        self.driver = driver

        self.customerCreate_id = "gwt-debug-button-menu-customer.addcustomer.customer.search"
        self.customerName_id = "gwt-debug-textbox-field-customer.customerNamecustomer.customer.details"
        self.customerCode_id = "gwt-debug-textbox-field-customer.customerCodecustomer.customer.details"
        self.customerSave_id = "gwt-debug-toolbar-icon-savecfservice.cfservice.result.for.customer"
        self.close_id="gwt-debug-toolbar-icon-closecfservice.cfservice.result.for.customer"

    def click_CreateCustomer(self):
        self.driver.find_element_by_id(self.customerCreate_id).click()

    def enter_CustomerName(self, customerName):
        self.driver.find_element_by_id(self.customerName_id).send_keys(customerName)

    def enter_CustomerCode(self,customerCode):
        self.driver.find_element_by_id(self.customerCode_id).send_keys(customerCode)

    def click_CustomerSave(self):
        self.driver.find_element_by_id(self.customerSave_id).click()

    def close(self):
        self.driver.find_element_by_id(self.close_id).click()
