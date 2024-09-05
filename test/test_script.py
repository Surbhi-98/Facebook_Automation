import sys
import time
sys.path.append('/home/cbnits/Documents/Facebook_Assignment/utility')
sys.path.append('/home/cbnits/Documents/Facebook_Assignment/pages')
sys.path.append('/home/cbnits/Documents/Facebook_Assignment/data')
import test_data
import Base_script
import Login_page
import Home_page
import Settings
import Logout



class Test_Script(Base_script.BasePage):

    def test_driver(self):
        self.driver.implicitly_wait(10)
        driver_title = self.driver.title
        print(driver_title)
        # assert driver_title == "Facebook – log in or sign up"
        assert driver_title == test_data.Test_Data.PAGE_TITLE
        self.message_logging(driver_title)

    def test_login_page(self):
        # user_email = test_data.Test_Data.USER_EMAIL
        # user_password = test_data.Test_Data.USER_PASSWORD
        # login_driver = Login_page.login_page_locators(self.driver, user_email, user_password)
        login_driver = Login_page.login_page_locators(self.driver, self.user_params)
        login_driver.username()
        login_driver.password()
        login_driver.submit_button()
        self.message_logging("Login Successfully")
    
    def test_Home_page(self):
        home_page_driver = Home_page.Home_page_locators(self.driver)
        # user = home_page_driver.user_name()
        # print(user)
        # assert user == "Surbhi Agrahari"
        # assert user == test_data.Test_Data.USER_NAME
        # self.message_logging("User name validate " + user)
        self.wait_clickable(Home_page.Home_page_locators.USER_PROFILE)
        home_page_driver.user_profile()
    
    def test_Setings(self):
        setting_driver = Settings.Setting_page_locators(self.driver)
        self.wait_clickable(Settings.Setting_page_locators.SETTING_PRIVACY)
        setting_driver.user_settings_privacy()
        self.wait_clickable(Settings.Setting_page_locators.SETTINGS)
        setting_driver.user_setting()
        
        time.sleep(5)
        user_email = setting_driver.user_email()
        # setting_driver.close_iframe()
        print(user_email)
        # assert user == "smilysurbhi@gmail.com"
        assert user_email == test_data.Test_Data.USER_EMAIL
        self.message_logging("Email validate " + user_email)

        user_name = setting_driver.user_name()
        setting_driver.close_iframe()
        setting_driver.close_iframe()
        print(user_name)
        assert user_name == test_data.Test_Data.USER_NAME
        self.message_logging("User name validate " + user_name)
        print("Assertion successfully Done")
        self.message_logging("Assertion successfully Done")
    
        self.wait_clickable(Settings.Setting_page_locators.USER_BLOCK)
        setting_driver.user_block()
        self.wait_clickable(Settings.Setting_page_locators.USER_BLOCK_EDIT)
        setting_driver.user_block_edit()
        self.wait_clickable(Settings.Setting_page_locators.USER_BLOCK_LIST)
        setting_driver.user_block_list()
   
        block_count = setting_driver.user_block_list_count()
        print(block_count)
        self.message_logging("Total no. of user blocked - " + str(block_count))
        
        self.wait_clickable(Settings.Setting_page_locators.USER_BLOCK_CLOSE)
        # self.wait_clickable(Settings.Setting_page_locators.USER_BLOCK_CLOSE)
        setting_driver.user_block_close()


    def test_logout(self):
        logout_driver = Logout.logout_page_locators(self.driver)
        logout_driver.user_logout_profile()
        self.wait_clickable(Logout.logout_page_locators.USER_LOGOUT)
        logout_driver.user_logout()
        self.message_logging("Logout Successfully")