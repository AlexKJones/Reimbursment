from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import keys
from time import sleep

from selenium.webdriver.common.keys import Keys


@given('The User is on the Home Page')
def get_to_home_page(context):
    driver: WebDriver = context.driver
    driver.get('file:///Users/alexjones/Desktop/RevatureTraining/reimbursment-client/home.html?')
    sleep(3)


@when('The User clicks on Log In')
def nav_click_login(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id('loginButton').click()
    sleep(9)


@then('The Employee fields should display undefined')
def verify_undfined(context):
    driver: WebDriver = context.driver
    nameo = driver.find_element_by_id("name")
    nameo = nameo.text
    assert nameo == "undefined"


@when('The User clicks on login field and then clicks the login button')
def log_in(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id("nameField").send_keys("5")
    driver.find_element_by_id('loginButton').click()
    sleep(9)


@then('The User should be logged in and showing data')
def verify_logged_in(context):
    driver: WebDriver = context.driver
    nameo = driver.find_element_by_id("name")
    nameo = nameo.text
    assert nameo == "Giorno Giovanna"


@given(u'The User is logged in')
def step_impl(context):
    driver: WebDriver = context.driver
    nameo = driver.find_element_by_id("name")
    nameo = nameo.text
    assert nameo == "Giorno Giovanna"


@when(u'The User puts bad credentials on request fields and then clicks the view button')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id("empReqId").send_keys("5")
    driver.find_element_by_id("seeRequestById").send_keys("5")
    driver.find_element_by_id('getRequests').click()
    sleep(6)


@then(u'The Notification field should read 404 request not found')
def step_impl(context):
    driver: WebDriver = context.driver
    nameo = driver.find_element_by_id("noti")
    nameo = nameo.text
    assert nameo == "404 request not found"


@when(u'The User puts in credentials on request fields and then clicks the view button')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys("5")
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys("1")
    driver.find_element_by_id('getRequests').click()
    sleep(9)


@then(u'The Notification field should read 200 succefully found request')
def step_impl(context):
    driver: WebDriver = context.driver
    nameo = driver.find_element_by_id("noti")
    nameo = nameo.text
    assert nameo == "200 succefully found request"


@when(u'The User clicks the log out button')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id('logoutButton').click()
    sleep(9)


@then(u'The Notification field should read Logged Out')
def step_impl(context):
    driver: WebDriver = context.driver
    nameo = driver.find_element_by_id("noti")
    nameo = nameo.text
    assert nameo == "Logged Out"

@given(u'The Supervisor is logged in')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("nameField").send_keys("4")
    driver.find_element_by_id('loginButton').click()
    sleep(9)

@when(u'The Supervisor views the request and clicks approve')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id("empReqId").send_keys("5")
    driver.find_element_by_id("seeRequestById").send_keys("1")
    driver.find_element_by_id('getRequests').click()
    sleep(3)
    driver.find_element_by_id('approve').click()
    sleep(5)


@then(u'The Notification field should read Approved by Supervisor awaiting Department Head approval')
def step_impl(context):
    driver: WebDriver = context.driver
    nameo = driver.find_element_by_id("noti")
    nameo = nameo.text
    assert nameo == "Approved by Supervisor awaiting Department Head approval"
    driver.find_element_by_id('logoutButton').click()


@given(u'The Department Head is logged in')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    sleep(2)
    driver.find_element_by_id("nameField").send_keys("1")
    driver.find_element_by_id('loginButton').click()
    sleep(9)


@when(u'The Department Head views the request and clicks approve')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id("empReqId").send_keys("5")
    driver.find_element_by_id("seeRequestById").send_keys("1")
    driver.find_element_by_id('getRequests').click()
    sleep(3)
    driver.find_element_by_id('approve').click()
    sleep(5)


@then(u'The Notification field should read Approved by DH awaiting approval from BenCo')
def step_impl(context):
    driver: WebDriver = context.driver
    nameo = driver.find_element_by_id("noti")
    nameo = nameo.text
    assert nameo == "Approved by DH awaiting approval from BenCo"
    driver.find_element_by_id('logoutButton').click()


@given(u'The BenCo is logged in')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    sleep(2)
    driver.find_element_by_id("nameField").send_keys("2")
    driver.find_element_by_id('loginButton').click()
    sleep(9)
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)


@when(u'The BenCo views the request and clicks approve')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys("5")
    driver.find_element_by_id("seeRequestById").send_keys("1")
    driver.find_element_by_id('getRequests').click()
    sleep(3)
    driver.find_element_by_id('approve').click()
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    sleep(5)

@then(u'The Notification field should read REQUEST APPROVED')
def step_impl(context):
    driver: WebDriver = context.driver
    nameo = driver.find_element_by_id("noti")
    nameo = nameo.text
    assert nameo == "REQUEST APPROVED"
    driver.find_element_by_id('logoutButton').click()
    sleep(3)

@given(u'The BenCo has approved the request')
def step_impl(context):
    driver: WebDriver = context.driver
    sleep(2)
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    sleep(2)
    driver.find_element_by_id("nameField").send_keys("5")
    driver.find_element_by_id('loginButton').click()
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    sleep(1)


@when(u'The user logs in and views request')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("nameField").send_keys("5")
    driver.find_element_by_id('loginButton').click()
    sleep(2)
    driver.find_element_by_id("empReqId").send_keys("5")
    driver.find_element_by_id("seeRequestById").send_keys("1")
    driver.find_element_by_id('getRequests').click()
    sleep(2)
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    sleep(9)


@then(u'The is_approved field should read true')
def step_impl(context):
    driver: WebDriver = context.driver
    nameo = driver.find_element_by_id("is_approved")
    nameo = nameo.text
    assert nameo == "true"
    driver.find_element_by_id('logoutButton').click()
    sleep(2)
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    sleep(5)

@given(u'The supervisor denies a request')
def step_impl(context):
    driver: WebDriver = context.driver
    sleep(2)
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    sleep(3)


@when(u'The supervisor logs in and views request inserts a 0 reason for denail and clicks deny')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("nameField").send_keys("4")
    driver.find_element_by_id('loginButton').click()
    sleep(4)
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    sleep(4)
    driver.find_element_by_id("empReqId").send_keys("5")
    driver.find_element_by_id("seeRequestById").send_keys("2")
    driver.find_element_by_id('getRequests').click()
    driver.find_element_by_id('denial_reason').send_keys("0")
    driver.find_element_by_id('deny').click()
    sleep(7)
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    sleep(2)
    driver.find_element_by_id('logoutButton').click()
    sleep(2)
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("nameField").send_keys("4")
    driver.find_element_by_id('loginButton').click()
    sleep(4)
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    sleep(2)
    driver.find_element_by_id("empReqId").send_keys("5")
    driver.find_element_by_id("seeRequestById").send_keys("2")
    driver.find_element_by_id('getRequests').click()
    sleep(9)
    driver.find_element_by_id("nameField").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("empReqId").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id("seeRequestById").send_keys(Keys.BACK_SPACE)
    sleep(2)


@then(u'The is_denied field should read true')
def step_impl(context):
    driver: WebDriver = context.driver
    nameo = driver.find_element_by_id("is_denied")
    nameo = nameo.text
    assert nameo == "true"
    sleep(8)

