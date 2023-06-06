import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def driver():
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://www.saucedemo.com/')
        yield driver
    except Exception as e:
        # Handle the exception or raise a custom exception
        print(f"Error occurred in setup fixture: {e}")
        raise
    finally:
        if driver:
            driver.quit()
