from pages.login import LoginPage
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
    logobj = LoginPage(drv)
    elem = logobj.check_portal_header()
    assert elem == "COMPLAINT PORTAL"

def test_tear_down(teardown):
    pass