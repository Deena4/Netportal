from ObjectRepository.NetportalLoginPage import LoginPage


class MainLogin_Test:
    username = "admin"
    password = "admin1001"

    def __init__(self, driver):
        self.driver = driver

    def Login_Test(self):

        login = LoginPage(self.driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()
        assert self.driver.title == "NETPortal"
        if self.driver.title == 'NETPortal':
            return True
        else:
            return False
