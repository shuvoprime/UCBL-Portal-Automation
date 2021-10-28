from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
from selenium.common.exceptions import NoSuchElementException , TimeoutException
from webdriver_manager import driver
sys.path.append(".")
from pages.wrapper import BasePage
from selenium.webdriver.chrome.options import Options
from tests.conftest import  setup
from resources.locators import task_management as tm
from resources.credentials import Constantinope as cp
from resources.locators import dashboard as dash


class Task_manage_create_task(BasePage):

    def __init__ (self,drv):
        self.drv = drv
        self.Wrap = BasePage(self.drv)

    def create_task_page_load(self):
        wrap = self.Wrap
        wrap.wait_until_element_clickable(10, tm.task_management_click_xpath).click()
        wrap.wait_until_element_clickable(10, tm.create_task_xpath).click()

        elem = wrap.wait_until_visibility_of_element_located(10, tm.create_task_header)
        return elem.text
    
    def create_task_complaint_issue(self):
        wrap = self.Wrap
        wrap.wd_Send_keys(tm.enter_wallet_number_xpath , cp.wallet_number)
        wrap.wait_until_element_clickable(10, tm.click_account_type_field_xpath).click()
        time.sleep(1)
        wrap.wait_until_element_clickable(10, tm.click_account_type_agent_xpath).click()
        #agent click porjonto hoise 
        time.sleep(1)
        wrap.wait_until_element_clickable(10, tm.click_issue_field_xpath).click()
        time.sleep(1)
        wrap.wait_until_element_clickable(10, tm.click_issue_complaint_xpath).click()
        time.sleep(1)
        wrap.wait_until_element_clickable(10, tm.click_mainhead_field_xpath).click()
        wrap.wait_until_element_clickable(10, tm.click_mainhead_complaints_against_agents_xpath).click()
        time.sleep(1)
        wrap.wait_until_element_clickable(10, tm.click_subhead_field_xpath).click()
        wrap.wait_until_element_clickable(10, tm.click_subhead_AgentsServiceRelatedIssue_xpath).click()
        elem = wrap.wait_until_visibility_of_element_located(10, tm.poe_header_xpath)
        return elem.text
    
class Task_manage_task_list(BasePage):

    def __init__ (self,drv):
        self.drv = drv
        self.Wrap = BasePage(self.drv)

    def task_list_visibility(self):
        wrap = self.Wrap
        wrap.wait_until_element_clickable(10, dash.dashboard_path_xpath).click()
        time.sleep(3)
        wrap.wait_until_element_clickable(10, tm.task_management_click_xpath).click()
        time.sleep(3)
        wrap.wait_until_element_clickable(10, tm.task_list_click_xpath).click()
        elem = wrap.wait_until_visibility_of_element_located(10, tm.task_list_header_xpath)
        elem1 = wrap.wait_until_visibility_of_element_located(10, tm.task_list_xpath)
        return elem.text,bool(elem1)

    def task_list_date_filter(self):
        wrap = self.Wrap
        
        wrap.wait_until_element_clickable(10, tm.task_list_from_date).click()
        wrap.wd_Send_keys_siimple(tm.task_list_from_date, cp.from_date_month)
        wrap.wd_Send_keys_siimple(tm.task_list_from_date, cp.from_date_day)
        wrap.wd_Send_keys_siimple(tm.task_list_from_date, cp.from_date_year)
        #time.sleep(3)
        wrap.wait_until_element_clickable(10, tm.task_list_to_date).click()
        wrap.wd_Send_keys_siimple(tm.task_list_to_date, cp.to_date_month)
        wrap.wd_Send_keys_siimple(tm.task_list_to_date, cp.to_date_day)
        wrap.wd_Send_keys_siimple(tm.task_list_to_date, cp.to_date_year)
        time.sleep(3)
        wrap.wait_until_element_clickable(10, tm.task_list_search_buttopn_xpath).click()
        elem = wrap.wait_until_visibility_of_element_located(10, tm.task_list_ticket_number_xpath)
        return elem.text
