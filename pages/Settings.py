from selenium.webdriver.common.by import By


class Setting_page_locators:
    #Locators
    SETTING_PRIVACY = (By.XPATH, "//span[text()='Settings & privacy']")
    SETTINGS = (By.XPATH, "//span[text()='Settings']")
    USER_EMAIL_ID = (By.XPATH, "//li[@data-testid='settings_section_email']//strong[contains(text(),'smilysurbhi@gmail.com')]")  #strong[text()='smilysurbhi@gmail.com'][@xpath="1"]
    USER_BLOCK = (By.XPATH, "//span[text()='Blocking']")
    USER_BLOCK_EDIT = (By.XPATH, "(//span[@class='b6ax4al1 lq84ybu9 hf30pyar om3e55n1 oshhggmv qm54mken'][normalize-space()='Edit'])[2]")
    USER_BLOCK_LIST = (By.XPATH, "(//span[text()='See your blocked list'])[1]")
    USER_BLOCK_LIST_COUNT = (By.XPATH, "//div[@class='h8391g91 m0cukt09 kpwa50dg ta68dy8c b6ax4al1']")
    USER_BLOCK_CLOSE = (By.XPATH, "//div[@aria-label = 'Close']/i[@class='gneimcpu oee9glnz']")
    USER_NAME = (By.CSS_SELECTOR, "li[data-testid='settings_section_name'] strong")

    def __init__(self, driver):
        self.driver = driver

    def user_settings_privacy(self):
        """"
        Click on USER SETTING PRIVACY
        """
        return self.driver.find_element(*Setting_page_locators.SETTING_PRIVACY).click()

    def user_setting(self):
        """"
        Click on SETTING
        """
        return self.driver.find_element(*Setting_page_locators.SETTINGS).click()

    def user_email(self):
        """"
        Switch to frame and fetch text from locator
        """
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[0])
        return self.driver.find_element(*Setting_page_locators.USER_EMAIL_ID).text

    def user_name(self):
        """"
        Fetch user name
        """
        # self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[0])
        return self.driver.find_element(*Setting_page_locators.USER_NAME).text

    def close_iframe(self):
        """"
        Close frame
        """
        self.driver.switch_to.default_content()

    def user_block(self):
        """"
        Click on block
        """
        return self.driver.find_element(*Setting_page_locators.USER_BLOCK).click()

    def user_block_edit(self):
        """"
        Click on user block edit
        """
        return self.driver.find_element(*Setting_page_locators.USER_BLOCK_EDIT).click()

    def user_block_list(self):
        """"
        Click on block list
        """
        return self.driver.find_element(*Setting_page_locators.USER_BLOCK_LIST).click()

    def user_block_list_count(self):
        """"
        Count no. of blocked user from list
        """
        count = self.driver.find_elements(*Setting_page_locators.USER_BLOCK_LIST_COUNT)
        return len(count)

    def user_block_close(self):
        """"
        Close block window
        """
        return self.driver.find_element(*Setting_page_locators.USER_BLOCK_CLOSE).click()
    


    


























        # driver = self.Homepage_locators()
        # # Name = driver.find_element(By.XPATH, "//strong[text()='Surbhi Agrahari']").text()
        # Name = driver.find_element(By.XPATH, "//strong[@xpath='1']").text
        # print(Name)
        # return Name
        # # time.sleep(4)
        # # username = driver.find_element(By.XPATH, "//strong[text()=' https://www.facebook.com/']").text
        # # print(username)
        # # # time.sleep(4)
        # # contact = driver.find_element(By.XPATH, "//span[text()='Primary: ']").text
        # # print(contact)

# obj = Setting_page_locators()
# # obj.test_chrome()
# # obj.username_locators()
# obj.Settingpage_locators()
