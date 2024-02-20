from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec

class LoginPage:
    __username=(By.ID,'input-username')
    __password=(By.ID,'input-password')
    __go_button=(By.NAME,'login-button')
    __err_msg =(By.XPATH,"//div[contains(text(),'Invalid')")

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,un):
        print('enter username:',un)
        self.driver.find_element(*self.__username).send_keys(un)

    def enter_password(self,pw):
        print('enter password:',pw)
        self.driver.find_element(*self.__password).send_keys(pw)

    def click_go_button(self):
        print('click go button')
        self.driver.find_element(*self.__go_button).click()

    def verify_err_msg(self,wait):
        print("err msg displayed")
        try:
         Ec.visibility_of_element_located(self.__err_msg)
         return True
        except:
            print("err msg is not display")
            return False