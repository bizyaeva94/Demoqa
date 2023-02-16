from locators.locators import TextBoxLocators
from pages.base_page import BasePage


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
