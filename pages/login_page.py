from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        username_input = self.driver.find_element(By.ID, "user-name")
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def is_login_successful(self):
        inventory_url = "https://www.saucedemo.com/inventory.html"
        return self.driver.current_url == inventory_url

    def get_error_message(self):
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        return error_message.text
