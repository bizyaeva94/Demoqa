from pages.elements_page import TextBoxPage
from generator.generator import Person
from time import sleep


class TestTextBox:
    def test_fill_all_fields(self, browser):
        link = 'https://demoqa.com/text-box'
        person = Person()
        name = person.full_name
        email = person.email
        current_address = person.current_address
        permanent_address = person.permanent_address
        page = TextBoxPage(browser)
        page.open(link)
        page.fill_all_fields(name, email, current_address, permanent_address)
        output_name = page.get_output()
        sleep(3)
        assert output_name[0] == name, 'Name is different'
        assert output_name[1] == email, 'Email is different'
        assert output_name[2] == current_address, 'Current address is different'
        assert output_name[3] == permanent_address, 'Permanent address is different'

# here is new feature


# here is the second feature