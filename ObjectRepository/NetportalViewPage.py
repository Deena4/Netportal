from selenium.webdriver.support.select import Select


class ViewPage:

    def __init__(self, driver):
        self.driver = driver

        self.createview_id="gwt-debug-button-menu-view.addview.view.search"
        self.viewName_id="gwt-debug-textbox-field-view.nameview.view.edit"
        self.viewType_id="gwt-debug-dropdown-field-view.typeview.view.edit"
        self.save_id="gwt-debug-toolbar-icon-saveview.element.view.element.result"

    def click_createview(self):
        self.driver.find_element_by_id(self.createview_id).click()

    def enter_viewName(self,ViewName):
        self.driver.find_element_by_id(self.viewName_id).send_keys(ViewName)

    def select_ShelfType(self, visibleText):
        element = self.driver.find_element_by_id(self.viewType_id)
        drop = Select(element)
        drop.select_by_visible_text(visibleText)

    def click_saveIcon(self):
        self.driver.find_element_by_id(self.save_id).click()
