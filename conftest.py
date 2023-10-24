import pytest
from selenium import webdriver
from utilities.test_data import TestData



@pytest.fixture(params=['chrome'])
def initialize_driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'edge':
        driver = webdriver.Edge()
    request.cls.driver = driver
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    driver.close()