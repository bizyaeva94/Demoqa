from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


class BasePage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def element_is_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def elements_are_present(self, how, what):
        try:
            self.browser.find_elements(how, what)
        except NoSuchElementException:
            return False
        return True

    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
