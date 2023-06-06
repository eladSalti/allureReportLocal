import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.mark.usefixtures("driver")
class TestLogin:
    @pytest.mark.tcid1
    def test_successful_login(self, login_page):
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        assert login_page.is_login_successful() is True, "There is an issue with the login method"

    @pytest.mark.tcid2
    def test_login_negative(self, login_page):
        login_page.enter_username("invalid_user")
        login_page.enter_password("wrong_password")
        login_page.click_login_button()
        assert login_page.is_login_successful() is False, "The login succeeded even though we entered wrong name and password"
        assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"

    @pytest.mark.tcid3
    def test_empty_username(self, login_page):
        login_page.enter_username("")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()
        assert login_page.get_error_message() == "Epic sadface: Username is required"

    @pytest.mark.tcid4
    def test_empty_password(self, login_page):
        login_page.enter_username("standard_user")
        login_page.enter_password("")
        login_page.click_login_button()
        assert login_page.get_error_message() == "Epic sadface: Password is required"
