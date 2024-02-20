import time

import pytest

from generic.basic_file import BaseTest
from generic.utility import Excel
from page.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains



class Test_invalid(BaseTest):
    @pytest.mark.run(oredr=2)
    def test_invalid_login(self):
        un = Excel.get_data(self.xl_path,'InvalidLogin', 2, 1)
        pw = Excel.get_data(self.xl_path, 'InvalidLogin', 2, 2)
        login_page = LoginPage(self.driver)
        login_page.enter_username(un)
        # 2. enter valid password
        login_page.enter_password(pw)
        # 3. click go
        login_page.click_go_button()
        time.sleep(4)

