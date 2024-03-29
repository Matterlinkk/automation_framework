import allure
from selenium.webdriver.support.select import Select

from pages.uitesting.qa_practice.selenium.base_page import BasePage
from selenium.webdriver.common.by import By

drop_down_list_args = (By.CSS_SELECTOR, 'select[id="id_choose_language"]')
submit_button_args = (By.CSS_SELECTOR, 'input[id="submit-id-submit"]')
result_text = (By.CSS_SELECTOR, 'p[id="result-text"]')


class SingleSelectPage(BasePage):
    def __init__(self, browser, marker):
        super().__init__(browser)
        self.marker = marker

    def open(self):
        with allure.step('Open the web page'):
            self.browser.get('https://www.qa-practice.com/elements/select/single_select')

    @property
    def __drop_down_list(self):
        with allure.step('Find dropdown list'):
            return self.find(drop_down_list_args)

    def change_drop_down_list_to_marker_value(self):
        with allure.step('Change dropdown state to {}'.format(self.marker)):
            state = Select(self.__drop_down_list)
            state.select_by_visible_text(self.marker)

    @property
    def __button(self):
        with allure.step('Find button'):
            return self.find(submit_button_args)

    def click_button(self):
        with allure.step('Click button'):
            self.__button.click()

    @property
    def result_text(self):
        with allure.step('Copy result text'):
            return self.find(result_text).text
