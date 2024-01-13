import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("Launching Chrome Browser")
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        print("Launching Firefox Browser")
        driver = webdriver.Firefox()
    elif browser == 'edge':
        print("Launching Edge Browser")
        driver = webdriver.Edge()
    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options= chrome_options)
        driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_metadata(metadata):
    metadata["Project Name"] = "CredKart"
    metadata["Environment"] = "QA Environment"
    metadata["Module"] = "User Profile"
    metadata["Tester"] = "Vikram"
    metadata.pop("Plugins", None)
