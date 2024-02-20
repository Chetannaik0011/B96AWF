from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    __logout=(By.XPATH,"//a[text()='Logout']")

    def __init__(self,driver):
        self.driver=driver

    def verify_home_page_is_displayed(self,wait):
        try:
            EC.visibility_of_element_located(self.__logout)
            print('Home page is dispalyed')
            return True
        except:
            print('Home page is NOT dispalyed')
            return False