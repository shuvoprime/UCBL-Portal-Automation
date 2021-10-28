from pages.dashboard import  Dashboard
import pytest
import sys
sys.path.append(".")

from selenium import webdriver
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from resources.credentials import Constantinope as cndemo

import time
import os

def test_check_login_homepage_header(setup):
    global drv
    drv = setup
    dashobj = Dashboard(drv)
    elem = dashobj.check_portal_header()
    assert elem == "COMPLAINT PORTAL"

#kaj kore na 
def test_check_login_notification():
    dashobj = Dashboard(drv)
    elem = dashobj.check_login_notification()
    assert elem == True

def test_check_username_role_header():
    dashobj = Dashboard(drv)
    elem = dashobj.check_username_role_showing()
    assert elem[0] == True
    assert elem[1] == True


    
def test_tear_down(teardown):
    pass