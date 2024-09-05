from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--user_email", action="store", default="********"
    )
    parser.addoption(
        "--password", action="store", default="*********"
    )
    parser.addoption(
        "--driver_path", action="store", default="/home/cbnits/Downloads/chromedriver"       
    )

@pytest.fixture(scope="class")
def driver_setup(request):
    BASE_URL = "https://www.facebook.com/"
    browser_name = request.config.getoption("browser_name")
    driver_path = request.config.getoption("driver_path")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    if browser_name == "chrome":
        # service_obj = Service("/home/cbnits/Downloads/chromedriver")
        service_obj = Service(driver_path)
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.get(BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class")
def passing_username_password(request):
    user_params = {"user_email" : request.config.getoption("user_email"),
                  "user_password" : request.config.getoption("password")}
    if user_params :
        request.cls.user_params= user_params
    yield


    