from pages.task_management import Task_manage_create_task
from pages.task_management import  Task_manage_task_list
import pytest
import sys
sys.path.append(".")

from selenium import webdriver
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from resources.credentials import Constantinope as cndemo

import time
import os

def test_create_task_page_load(setup):
    global drv
    drv = setup
    tmobj = Task_manage_create_task(drv)
    elem = tmobj.create_task_page_load()
    assert elem == "Create Task"

def test_create_task_complaint():
    tmobj = Task_manage_create_task(drv)
    elem = tmobj.create_task_complaint_issue()
    #task creation porjonto hoise 
    assert elem == "POEs:"

def test_task_list():
    tmobj = Task_manage_task_list(drv)
    elem = tmobj.task_list_visibility()
    assert elem[0] == "Task List"
    assert elem[1] == True

def test_date_filter():
    tmobj = Task_manage_task_list(drv)
    elem = tmobj.task_list_date_filter()
    assert elem == "202110000010"

    
def test_tear_down(teardown):
    pass