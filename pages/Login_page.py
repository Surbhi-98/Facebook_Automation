from selenium.webdriver.common.by import By


class login_page_locators:
    #Locators
    EMAIL_ID = (By.XPATH, "//input[@type='text']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    SUBMIT = (By.NAME, "login")

    def __init__(self, driver, user_params):
        self.driver = driver
        # self.user_email = user_email
        # self.user_password = user_password
        self.user_params = user_params


    def username(self):
        """"
        Enter Your EMAIL
        """
        # return self.driver.find_element(*login_page_locators.EMAIL_ID).send_keys("********")
        return self.driver.find_element(*login_page_locators.EMAIL_ID).send_keys(self.user_params["user_email"])

    def password(self):
        """"
        Enter Your PASSWORD
        """
        # return self.driver.find_element(*login_page_locators.PASSWORD).send_keys("********")
        return self.driver.find_element(*login_page_locators.PASSWORD).send_keys(self.user_params["user_password"])

    def submit_button(self):
        """"
        Click SUBMIT
        """
        return self.driver.find_element(*login_page_locators.SUBMIT).click()
