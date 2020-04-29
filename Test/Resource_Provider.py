import time
from ObjectRepository.NetportalHomePage import HomePage
from ObjectRepository.NetportalProviderPage import ProviderPage


class TestProvider1:
    # DATA
    ProviderName = "TestProvider28"
    ProviderCode = "118"

    def __init__(self, driver):
        self.driver = driver

    def TCP_AUT_GUI_RES_PRV_000_000_001_00002_POS_Test(self):
        home = HomePage(self.driver)
        time.sleep(3)
        home.click_Resources()
        time.sleep(3)
        home.click_Provider()

        provider = ProviderPage(self.driver)
        time.sleep(3)
        provider.click_CreateProvider()
        time.sleep(4)
        provider.enter_ProviderName(self.ProviderName)
        time.sleep(3)
        provider.enter_ProviderCode(self.ProviderCode)
        time.sleep(3)
        provider.click_saveIcon()
        time.sleep(3)
        provider.close()
        time.sleep(3)