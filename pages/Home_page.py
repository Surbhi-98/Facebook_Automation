from selenium.webdriver.common.by import By

class Home_page_locators:
    #Locators
    USER_PROFILE = (By.XPATH, "(//*[name()='image'])[1]")
    # PROFILE_NAME = (By.XPATH, "//span[@class='b6ax4al1 lq84ybu9 hf30pyar om3e55n1'][starts-with(text(),'Surbhi Agrahari')]")

    def __init__(self, driver):
        self.driver = driver

    # def user_name(self):
    """"
    Fetch user name
    """
    #     user = self.driver.find_element(*Home_page_locators.PROFILE_NAME).text
    #     return user

    def user_profile(self):
        """"
        Click on User Profile link
        """
        return self.driver.find_element(*Home_page_locators.USER_PROFILE).click()

