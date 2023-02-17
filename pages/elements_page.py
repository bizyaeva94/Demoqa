from locators.locators import TextBoxLocators
from locators.locators import CheckBoxLocators
from pages.base_page import BasePage
import random


class TextBoxPage(BasePage):

    def fill_all_fields(self, name, email, current_address, permanent_address):
        self.browser.find_element(*TextBoxLocators.FULL_NAME).send_keys(name)
        self.browser.find_element(*TextBoxLocators.EMAIL).send_keys(email)
        self.browser.find_element(*TextBoxLocators.CURRENT_ADDRESS).send_keys(current_address)
        self.browser.find_element(*TextBoxLocators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.browser.find_element(*TextBoxLocators.SUBMIT_BUTTON).click()

    def get_output(self):
        output_name = self.browser.find_element(*TextBoxLocators.OUTPUT_NAME).text.split(':')[1]
        output_email = self.browser.find_element(*TextBoxLocators.OUTPUT_EMAIL).text.split(':')[1]
        output_current_address = self.browser.find_element(*TextBoxLocators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        output_permanent_address = self.browser.find_element(*TextBoxLocators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
        return output_name, output_email, output_current_address, output_permanent_address


class CheckBoxPage(BasePage):

    def expand_all(self):
        self.browser.find_element(*CheckBoxLocators.EXPAND_ALL).click()
        self.elements_are_present(*CheckBoxLocators.EXPANDED_LIST)

    def click_random_checkboxes(self):
        item_list = self.browser.find_elements(*CheckBoxLocators.CHECKBOX_TITLE)
        for _ in range(random.randint(1, 10)):
            item = item_list[random.randint(1, 16)]
            self.scroll_to_element(item)
            item.click()

    def get_checked_checkboxes(self):
        checked_items = self.browser.find_elements(*CheckBoxLocators.CHECKED_ITEM)
        checked_titles = []
        for item in checked_items:
            checked_titles.append(item.text)
        return str(checked_titles).lower()

    def get_output_result(self):
        result = self.browser.find_elements(*CheckBoxLocators.SELECTED_RESULT)
        result_titles = []
        for item in result:
            result_titles.append(item.text)
        return str(result_titles).lower()
