import pytest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import time


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://github.com/login")
    login_elem = driver.find_element(ChromeDriverManager.ID, "login_field")
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")
    time.sleep(3)
    driver.close()
