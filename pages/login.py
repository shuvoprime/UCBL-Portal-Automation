from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
from selenium.common.exceptions import NoSuchElementException , TimeoutException
sys.path.append(".")
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from tests.conftest import  setup
from resources.locators import common_locators as cl
from resources.locators import dashboard as dash

class LoginPage(BasePage):
    def __init__ (self,drv):
        self.drv = drv
        self.Wrap = BasePage(self.drv)


    def check_portal_header(self):
        wrap = self.Wrap
        elem = wrap.wait_until_visibility_of_element_located(10, cl.homepage_header)
        return elem.text

    def check_username_role_showing(self):
        wrap = self.Wrap
        elem = wrap.wait_until_visibility_of_element_located(10, dash.username_header_xpath)
        elem1 = wrap.wait_until_visibility_of_element_located(10, dash.role_header_xpath)
        return bool(elem),bool(elem1)