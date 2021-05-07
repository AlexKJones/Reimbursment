from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.reimbursment_home import Reimbursment


def before_all(context):
    driver: WebDriver = webdriver.Chrome(
        "/Users/alexjones/Desktop/RevatureTraining/chromedriver"
    )
    main_page = Reimbursment(driver)

    context.driver = driver
    context.main_page = main_page
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
