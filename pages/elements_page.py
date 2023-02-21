from pages.base_page import BasePage
import random
from locators.locators import *
from time import sleep


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


class WebTablePage(BasePage):
    col_list = None
    counter = 0

    def sort_table(self):
        self.counter = 0
        header = self.browser.find_elements(*WebTableLocators.HEADER)
        for element in header[:-1]:
            element.click()
            self.check_sorting_table(self.counter)
            yield self.col_list
            self.counter += 1

    def check_sorting_table(self, counter):
        rows = self.browser.find_elements(*WebTableLocators.ROW)
        self.col_list = []
        for row in rows:
            cell = row.find_elements(*WebTableLocators.COL)[counter]
            if cell.text != ' ':
                self.col_list.append(cell.text)

    def sort_list(self):
        rows = self.browser.find_elements(*WebTableLocators.ROW)
        col_list_2 = []
        for row in rows:
            cell = row.find_elements(*WebTableLocators.COL)[self.counter]
            if cell.text != ' ':
                if cell.text.isdigit():
                    col_list_2.append(int(cell.text))
                else:
                    col_list_2.append(cell.text)
        list.sort(col_list_2)
        return [str(elem) for elem in col_list_2]

    def sort_table_reverse(self):
        self.counter = 0
        header = self.browser.find_elements(*WebTableLocators.HEADER)
        for element in header[:-1]:
            element.click()
            element.click()
            self.check_sorting_table(self.counter)
            yield self.col_list
            self.counter += 1

    def sort_list_reverse(self):
        rows = self.browser.find_elements(*WebTableLocators.ROW)
        col_list_2 = []
        for row in rows:
            cell = row.find_elements(*WebTableLocators.COL)[self.counter]
            if cell.text != ' ':
                if cell.text.isdigit():
                    col_list_2.append(int(cell.text))
                else:
                    col_list_2.append(cell.text)
        list.sort(col_list_2, reverse=True)
        return [str(elem) for elem in col_list_2]

    def count_rows(self):
        row = self.browser.find_elements(*WebTableLocators.NOT_EMPTY_ROW)
        number_of_rows = len(row)
        return number_of_rows

    def click_add_button(self):
        self.browser.find_element(*WebTableLocators.ADD_BUTTON).click()
        self.element_is_present(*WebTableLocators.REGISTRATION_FORM)

    def fill_registration_form(self, first_name: str, last_name: str, age: int, email: str, salary: int, department: str):
        self.browser.find_element(*WebTableLocators.INPUT_FIRST_NAME).send_keys(first_name)
        self.browser.find_element(*WebTableLocators.INPUT_LAST_NAME).send_keys(last_name)
        self.browser.find_element(*WebTableLocators.INPUT_AGE).send_keys(age)
        self.browser.find_element(*WebTableLocators.INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*WebTableLocators.INPUT_SALARY).send_keys(salary)
        self.browser.find_element(*WebTableLocators.INPUT_DEPARTMENT).send_keys(department)

    def submit_form(self):
        self.browser.find_element(*WebTableLocators.SUBMIT_BUTTON).click()

    def get_person_data_from_table(self, number):
        row = self.browser.find_elements(*WebTableLocators.ROW)[number].text.split("\n")
        return row

    def get_required_attr(self):
        required_first_name = self.browser.find_element(*WebTableLocators.INPUT_FIRST_NAME).get_attribute('required')
        required_last_name = self.browser.find_element(*WebTableLocators.INPUT_LAST_NAME).get_attribute('required')
        required_age = self.browser.find_element(*WebTableLocators.INPUT_AGE).get_attribute('required')
        required_email = self.browser.find_element(*WebTableLocators.INPUT_EMAIL).get_attribute('required')
        required_salary = self.browser.find_element(*WebTableLocators.INPUT_SALARY).get_attribute('required')
        required_department = self.browser.find_element(*WebTableLocators.INPUT_DEPARTMENT).get_attribute('required')
        return [required_first_name, required_last_name, required_age, required_email, required_salary, required_department]
