from pages.elements_page import CheckBoxPage
from time import sleep


class TestCheckBox:
    def test_fill_all_fields(self, browser):
        link = 'https://demoqa.com/checkbox'
        page = CheckBoxPage(browser)
        page.open(link)
        page.expand_all()
        page.click_random_checkboxes()
        checked_titles = page.get_checked_checkboxes()
        result_titles = page.get_output_result()
        assert checked_titles == result_titles, "Output result does not match checked checkboxes"
