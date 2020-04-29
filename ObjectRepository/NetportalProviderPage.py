class ProviderPage:

    def __init__(self, driver):
        self.driver = driver

        self.createProvider_id ="gwt-debug-button-menu-provider.addcustomer.provider.result"
        self.providerName_id="gwt-debug-textbox-field-customer.customerNamecustomer.provider.details"
        self.providerCode_id="gwt-debug-textbox-field-customer.customerCodecustomer.provider.details"
        self.save_id="gwt-debug-toolbar-icon-savegenerator.range.object.association.detail.form.assoc.in.object"
        self.close_id="gwt-debug-toolbar-icon-closegenerator.range.object.association.detail.form.assoc.in.object"


    def click_CreateProvider(self):
        self.driver.find_element_by_id(self.createProvider_id).click()

    def enter_ProviderName(self,providerName):
        self.driver.find_element_by_id(self.providerName_id).send_keys(providerName)

    def enter_ProviderCode(self,providerCode):
         self.driver.find_element_by_id(self.providerCode_id).send_keys(providerCode)

    def click_saveIcon(self):
        self.driver.find_element_by_id(self.save_id).click()

    def close(self):
        self.driver.find_element_by_id(self.close_id).click()