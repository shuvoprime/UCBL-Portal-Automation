#import pytest
import sys
sys.path.append(".")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.wrapper import BasePage
from resources.credentials import Constantinope as cndemo
from selenium.webdriver.chrome.options import Options
from resources.locators import common_locators as cl
import time

global driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
#request.cls.driver = web_driver
driver.maximize_window()
driver.get(cndemo.complain_portal)
wrap = BasePage(driver)
wrap.wd_Send_keys_siimple(cl.signin_username_xpath , cndemo.username)
wrap.wd_Send_keys_siimple(cl.signin_password_xpath , cndemo.password)
wrap.wd_click_simple(cl.signin_login_xpath)
