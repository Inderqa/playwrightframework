import pytest
from pytest_playwright.pytest_playwright import browser, playwright, context

from pageObject.flipkart import *
from playwright.sync_api import Page

from utilities.base_class_utils import BaseClass

@pytest.mark.usefixtures("start_browser_with_tracing")
def test_flipkart_aut(start_browser_with_tracing):
    page = start_browser_with_tracing
    base = BaseClass(page)
    base.go_to_url("https://www.flipkart.com/")
    flipkart = flipkartHome(page)
    flipkart.flipkart_get_mobile_price_with_mobile_name("Redmi 5A (Blue, 16 GB)")


def test_flipkart_aut(start_browser_with_tracing):
    page = start_browser_with_tracing
    base = BaseClass(page)
    base.go_to_url("https://www.flipkart.com")
    flipkart = flipkartHome(page)
    flipkart.flipkart_mobile_name_price_in_ascending_order("Redmi 5A (Blue, 16 GB)")

    # lg_locators= page.locator("xpath=//div[contains(@class,'yKfJKb row')]//div[contains(@class,'KzDlHZ')]").all()
    # import pdb
    # pdb.set_trace()
    # lg_price = page.locator("x").all()
    # lg_washing_price = []
    # lg_wash = {name:price}
#
#     for i in lg_locators:
#         name =
#         price = (//sibiling::).text_content
#         print(lg_washing
#
#     for key,value in lg _s:
#         if key[value] >
#
#
#
#
# browser = playwright.chromium.launch() >> open the browser
# context = browser.new_context() >> it will open new session(meaning opening new broswer new tab)
# page = context.new_page() >> page.goto(google.com)












