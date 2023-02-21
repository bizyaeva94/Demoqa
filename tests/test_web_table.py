from pages.elements_page import WebTablePage
from generator.generator import Person
import random
from time import sleep


class TestSortTable:
    def test_sort_table(self, browser):
        link = "https://demoqa.com/webtables"
        page = WebTablePage(browser)
        page.open(link)
        sorting_result = page.sort_table()
        while True:
            try:
                assert next(sorting_result) == page.sort_list()
            except StopIteration:
                break

    def test_sort_table_reverse(self, browser):
        link = "https://demoqa.com/webtables"
        page = WebTablePage(browser)
        page.open(link)
        sorting_result = page.sort_table_reverse()
        while True:
            try:
                assert next(sorting_result) == page.sort_list_reverse()
            except StopIteration:
                break


class TestAddPerson:

    def test_add_person(self, browser):
        link = "https://demoqa.com/webtables"
        page = WebTablePage(browser)
        page.open(link)
        for _ in range(2):
            person = Person()
            number = page.count_rows()
            page.click_add_button()
            data_for_registration = [
                person.first_name, person.last_name, str(random.randint(18, 65)), person.email,
                str(random.randint(10000, 50000)), person.job
            ]
            page.fill_registration_form(*data_for_registration)
            page.submit_form()
            new_person_data = page.get_person_data_from_table(number)
            sleep(5)
            assert new_person_data == data_for_registration, "Data of new added person not equal registration data"

    def test_add_empty_form(self, browser):
        link = "https://demoqa.com/webtables"
        page = WebTablePage(browser)
        page.open(link)
        page.click_add_button()
        page.submit_form()
        required_field = page.get_required_attr()
        assert required_field[0] == 'true'
        assert required_field[1] == 'true'
        assert required_field[2] == 'true'
        assert required_field[3] == 'true'
        assert required_field[4] == 'true'
        assert required_field[5] == 'true'
