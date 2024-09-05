from selenium.webdriver.common.by import By


class logout_page_locators:
    #Locators
    USER_BACK = (By.XPATH, "(//*[name()='image'])[1]")
    USER_LOGOUT = (By.XPATH, "//span[text()='Log Out']")

    def __init__(self, driver):
        self.driver = driver

    def user_logout_profile(self):
        """"
        Click on user profile
        """
        return self.driver.find_element(*logout_page_locators.USER_BACK).click()

    def user_logout(self):
        """"
        Click on LOGOUT button
        """
        return self.driver.find_element(*logout_page_locators.USER_LOGOUT).click()

