from selenium.webdriver.common.by import By


class TextBoxLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input#userName")
    EMAIL = (By.CSS_SELECTOR, "input#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea#permanentAddress")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button#submit")
    OUTPUT_NAME = (By.CSS_SELECTOR, "#output #name")
    OUTPUT_EMAIL = (By.CSS_SELECTOR, "#output #email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
