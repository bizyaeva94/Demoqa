from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


class BasePage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
