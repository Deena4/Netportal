class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_id = "j_username"
        self.password_id = "j_password"
        self.login_id = "j_login"
        self.userNameText_xpath = "//div[contains(text(),'Username')]"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_id).click()

    def get_UserNameText(self):
        self.driver.find_element_by_xpath(self.userNameText_xpath).getAttribute("admin")
