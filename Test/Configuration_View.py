import time
from ObjectRepository.NetportalHomePage import HomePage
from ObjectRepository.NetportalViewPage import ViewPage


class TestView1:
    # DATA
    ViewName = "view58"
    visibleText = "Public"

    def __init__(self,driver):
        self.driver = driver

    def TCP_AUT_GUI_CFG_VWS_000_000_001_00004_POS_Test(self):
        home = HomePage(self.driver)
        home.click_Dashboard()
        time.sleep(4)
        home.click_view()

        view = ViewPage(self.driver)
        time.sleep(3)
        view.click_createview()
        time.sleep(3)
        view.enter_viewName(self.ViewName)
        time.sleep(3)
        view.select_ShelfType(self.visibleText)
        time.sleep(3)
        view.click_saveIcon()
        time.sleep(3)

        home.click_Dashboard()
        time.sleep(3)
        home.click_view()
