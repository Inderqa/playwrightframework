import json
import os

import allure
from playwright.sync_api import Page, expect, Playwright
from pytest_playwright.pytest_playwright import context, browser
import pytest

from pageObject.dashboard import dashboard
from pageObject.loginPage import loginpage

# with open('test_data/creds.json') as f:
#     test_data = json.load(f)
#     print(test_data)
#     user_credentials_list = test_data['user_credentials']
#
# @pytest.mark.parametrize('user_credentials',user_credentials_list)
# def test_e2e_web(playwright:Playwright,user_credentials):
#     browser=playwright.chromium.launch(headless=False)
#     context=browser.new_context()
#     page=context.new_page()
#     user_email = user_credentials['userEmail']
#     user_password =user_credentials['userPassword']
#     login = loginpage(page)
#     login.navigation()
#     dashboard_page = login.login(user_email, user_password)
#     screenshot = page.screenshot()
#     allure.attach(screenshot, name="DASHBOARD_PAGE", attachment_type=allure.attachment_type.PNG)
#     order_hist = dashboard_page.dashboard_orders()
#     order_det = order_hist.order_history_view()
#     order_det.order_complete_text()



def test_pracs(playwright:Playwright):
    user_data_dir = os.path.abspath("../user-data")  # Temp user profile

    context = playwright.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False,
        args=["--start-maximized"]
    )

    page = context.pages[0] if context.pages else context.new_page()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    page.locator("//input[@id='name']").fill("hello")
    page.locator("//select[@id='dropdown-class-example']").click()
    gen = page.query_selector_all("//select[@id='dropdown-class-example']/option")
    for option in gen:
        value = option.get_attribute("value")
        if value == "option2":
            option.click()


