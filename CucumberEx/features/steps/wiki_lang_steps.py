from behave import given, when, then
from selenium.webdriver.chrome.webdriver import WebDriver


@given('The User is on the Wikipedia Home Page')
def get_to_wiki_home(context):
    driver: WebDriver = context.driver
    driver.get('https://www.wikipedia.org/')


@when('The User clicks on English')
def nav_to_english(context):
    driver: WebDriver = context.driver
    driver.find_element_by_id('js-link-box-en').click()


@then('The User should be on the English Home Page')
def verify_on_english_page(context):
    driver: WebDriver = context.driver
    assert driver.title == "Wikipedia, the free encyclopedia"


@given('The User is on the Wikipedia Home Page')
def get_to_wiki_home(context):
    driver: WebDriver = context.driver
    driver.get('https://www.wikipedia.org/')


@when('The User clicks on Spanish')
def nav_to_spanish(context):
    context.wiki_home_page.spanish().click()


@then('The User should be on the Spanish Home Page')
def verify_on_spanish_page(context):
    driver: WebDriver = context.driver
    assert driver.title == "Wikipedia, la enciclopedia libre"
