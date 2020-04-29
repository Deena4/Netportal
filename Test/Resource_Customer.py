import time
from ObjectRepository.NetportalCustomerPage import CustomerPage
from ObjectRepository.NetportalHomePage import HomePage


class TestCustomer1:
    # DATA
    CustomerName = "TestCustomer62"
    CustomerCode = "162"

    def __init__(self, driver):
        self.driver = driver

    def TCP_AUT_GUI_RES_CUS_000_000_001_00001_POS_Test(self):
        home = HomePage(self.driver)
        time.sleep(3)
        home.click_Resources()
        time.sleep(3)
        home.click_Customers()

        customer = CustomerPage(self.driver)
        time.sleep(3)
        customer.click_CreateCustomer()
        time.sleep(3)
        customer.enter_CustomerName(self.CustomerName)
        time.sleep(3)
        customer.enter_CustomerCode(self.CustomerCode)
        time.sleep(3)
        customer.click_CustomerSave()
        time.sleep(4)
        customer.close()
        time.sleep(4)
        home.click_Dashboard()
        time.sleep(7)
        home.click_view()

