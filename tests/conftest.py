import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()