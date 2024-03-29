import allure

from pages.uitesting.qa_practice.selenium.base_page import BasePage
from selenium.webdriver.common.by import By

checkbox_args = (By.CSS_SELECTOR, 'input[class="form-check-input"]')
submit_button = (By.CSS_SELECTOR, 'input[class="btn btn-primary"]')
result_text = (By.CSS_SELECTOR, 'p[id="result-text"]')


class SingleCheckboxPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        with allure.step('Open the web page'):
            self.browser.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')

    @property
    def __checkbox(self):
        with allure.step('Find checkbox'):
            return self.find(checkbox_args)

    def checkbox_click(self):
        with allure.step('Click checkbox'):
            self.__checkbox.click()

    @property
    def __button(self):
        with allure.step('Find button'):
            return self.find(submit_button)

    def button_click(self):
        with allure.step('Click button'):
            self.__button.click()

    def result_text(self):
        with allure.step('Copy result text'):
            return self.find(result_text).text
