import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver(request):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    request.driver = driver
    yield driver
    driver.quit()