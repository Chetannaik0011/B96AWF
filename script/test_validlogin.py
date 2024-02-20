import pytest

from generic.basic_file import BaseTest
from page.login_page import LoginPage
from page.home_page import HomePage
from generic.utility import Excel

class Test_ValidLogin(BaseTest):
    @pytest.mark.run(oredr=1)
    def test_valid_login(self):
        un=Excel.get_data(self.xl_path,'ValidLogin',2,1)
        pw=Excel.get_data(self.xl_path,'ValidLogin',2,2)
        # 1. enter valid username
        login_page = LoginPage(self.driver)
        login_page.enter_username(un)
        #2. enter valid password
        login_page.enter_password(pw)
        # 3. click go
        login_page.click_go_button()
        # # 4. verify that homepage is displayed
        home_page = HomePage(self.driver)
        result = home_page.verify_home_page_is_displayed(self.wait)
        assert result