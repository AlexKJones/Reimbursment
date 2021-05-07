from selenium.webdriver.chrome.webdriver import WebDriver


class Reimbursment:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_name_field(self):
        return self.driver.find_element_by_id("nameField")

    def login_name_button(self):
        return self.driver.find_element_by_id('loginButton')

    def logout_button(self):
        return self.driver.find_element_by_id('logoutButton')

    def request_name_field(self):
        return self.driver.find_element_by_id("empReqId")

    def request_id_field(self):
        return self.driver.find_element_by_id("seeRequestById")

    def view_request(self):
        return self.driver.find_element_by_id('getRequests')

    def approve_button(self):
        return self.driver.find_element_by_id('approve')

    def get_more_info_button(self):
        return self.driver.find_element_by_id('getMoreInfo')

    def denial_reason_field(self):
        return self.driver.find_element_by_id('denial_reason')

    def deny_button(self):
        return self.driver.find_element_by_id('deny')

    def addInfo_button(self):
        return self.driver.find_element_by_id('addInfo')

    def add_info_field(self):
        return self.driver.find_element_by_id('add_info')

    def changeFunds_button(self):
        return self.driver.find_element_by_id('changeFunds')

    def change_funds_field(self):
        return self.driver.find_element_by_id('change_funds')
