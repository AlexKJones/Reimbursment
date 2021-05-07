from time import sleep

import driver as driver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from pages.reimbursment_home import Reimbursment
WebElement = driver.find_element_by_name("q")
driver: WebDriver = webdriver.Chrome(
    "/Users/alexjones/Desktop/RevatureTraining/chromedriver")

main_page = Reimbursment(driver)

try:
    # Login User That Created Request
    driver.get("file:///Users/alexjones/Desktop/RevatureTraining/reimbursment-client/home.html?")
    sleep(1)
    main_page.login_name_field().send_keys("5")
    sleep(2)
    main_page.login_name_button().send_keys(Keys.ENTER)
    sleep(2)
    # assert

    # Get Request Data
    main_page.request_name_field().send_keys("5")
    main_page.request_id_field().send_keys("1")
    sleep(1)
    main_page.view_request().send_keys(Keys.ENTER)
    sleep(3)
    # assert driver.find_element_by_id("req_name") == "Giorno Giovanna"

    # Check Buttons dont work
    main_page.denial_reason_field().send_keys("5")
    main_page.add_info_field().send_keys("1")
    main_page.change_funds_field().send_keys("1")
    sleep(2)
    main_page.approve_button().send_keys(Keys.ENTER)
    sleep(2)
    main_page.get_more_info_button().send_keys(Keys.ENTER)
    sleep(2)
    main_page.deny_button().send_keys(Keys.ENTER)
    sleep(2)
    main_page.addInfo_button().send_keys(Keys.ENTER)
    sleep(2)
    main_page.changeFunds_button().send_keys(Keys.ENTER)
    sleep(4)
    # assert driver.find_element_by_id("req_name") == "Giorno Giovanna"




except AssertionError:
    print("Getting information failure")
else:
    print("Test Passed - No assertions failed.")
finally:
    driver.close()