from .base_page import BasePage
from selenium.webdriver.common.by import By

class TextBoxPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, 'https://demoqa.com/text-box', timeout)

        self.driver.get(self.url)

        self.full_name = self.driver.find_element(By.ID, 'userName')
        self.email = self.driver.find_element(By.ID, 'userEmail')
        self.current_address = self.driver.find_element(By.CSS_SELECTOR, 'textarea#currentAddress.form-control')
        self.permanent_address = self.driver.find_element(By.CSS_SELECTOR, 'textarea#permanentAddress.form-control')
        self.submit_button = self.driver.find_element(By.ID, 'submit')

    def enter_fullname(self, value):
        self.full_name.send_keys(value)

    def enter_email(self, value):
        self.email.send_keys(value)

    def enter_curraddress(self, value):
        self.current_address.send_keys(value)

    def enter_permaddress(self, value):
        self.permanent_address.send_keys(value)

    def btn_click(self):
        self.submit_button.click()




