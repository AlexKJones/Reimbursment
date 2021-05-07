from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from CucumberEx.features.pages.wiki_home import WikiHomePage


def before_all(context):
    driver: WebDriver = webdriver.Chrome(
        "/Users/alexjones/Desktop/RevatureTraining/chromedriver"
    )
    wiki_home_page = WikiHomePage(driver)

    context.driver = driver
    context.wiki_home_page = wiki_home_page
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
