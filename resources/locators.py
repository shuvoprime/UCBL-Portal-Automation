class common_locators:
    
    signin_username_xpath = "//input[@id='username']"
    signin_password_xpath = "//input[@id='password']"
    signin_login_xpath = "//button[@type='submit']"

    homepage_header = "//span[contains(@class,'text-white')]"

class dashboard:
    username_header_xpath = "//b[normalize-space()='Username:']"
    role_header_xpath = "//b[normalize-space()='Role:']"
    dashboard_header_xpath = "//h4[@class='page-title']"
    last_30_days_xpath = "//h4[@class='card-title mb-4']"
    login_notification = '//*[@id="root"]/div[1]/div'
    dashboard_path_xpath = "//span[normalize-space()='Dashboard']"

class task_management:
    task_management_click_xpath = '/html/body/div/div[2]/div[2]/div[1]/div[1]/ul/li[2]/a/span' 
    #"//span[normalize-space()='Task Management']"
    create_task_xpath = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]"
    #create_task_header = '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/h4'
    create_task_header = "//h4[@class='page-title']"
    enter_wallet_number_xpath = "//input[@name='wallet_number']"
    click_account_type_field_xpath = '/html/body/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/form/div[1]/div[2]/div/div/div/div[2]/div'
    #'//*[@id="wrapper"]/div[3]/div/div[2]/div[2]/div/div/div/form/div[1]/div[2]/div/div/div/div[1]'
    click_account_type_agent_xpath = '/html/body/div[2]/div/div/div[1]'
    click_issue_field_xpath = '/html/body/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/form/div[2]/div[1]/div/div/div/div[2]/div'
    click_issue_complaint_xpath = "/html/body/div[2]/div/div/div[1]"
    click_mainhead_field_xpath = "/html/body/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/form/div[2]/div[2]/div/div/div/div[2]/div"
    click_mainhead_complaints_against_agents_xpath = "/html/body/div[2]/div/div/div[1]"
    click_subhead_field_xpath = "/html/body/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/form/div[2]/div[3]/div/div/div/div[2]/div"
    click_subhead_AgentsServiceRelatedIssue_xpath = '/html/body/div[2]/div/div/div[1]'
    poe_header_xpath = "/html/body/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/form/h6"

    task_list_click_xpath = '/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[2]/ul[1]/li[2]/a[1]'
    task_list_header_xpath = '//*[@id="wrapper"]/div[3]/div/div[2]/div[1]/div/div[1]/h4'
    task_list_xpath = '/html/body/div/div[2]/div[3]/div/div[2]/div[3]/div'

    task_list_from_date = "/html/body/div/div[2]/div[3]/div/div[2]/div[2]/div/form/div[1]/div[1]/input"
    task_list_to_date = "/html/body/div/div[2]/div[3]/div/div[2]/div[2]/div/form/div[1]/div[2]/input"
    task_list_search_buttopn_xpath = "//button[@type='submit']"
    task_list_ticket_number_xpath = "//div[contains(text(),'202110000010')]"
