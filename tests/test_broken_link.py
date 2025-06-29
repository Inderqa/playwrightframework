import time

import pytest
import requests
from pytest_playwright.pytest_playwright import browser, playwright, context

from pageObject.flipkart import *
from playwright.sync_api import Page

from utilities.base_class_utils import BaseClass



def test_broken_link(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    base = BaseClass(page)
    base.go_to_url("https://demoqa.com/broken")
    time.sleep(2)

    links = page.locator("//div[@class='col-12 mt-4 col-md-6']//div/a")

    count = links.count()
    print(f"Total links found: {count}")

    for i in range(count):
        link = links.nth(i)
        text = link.text_content()
        href = link.get_attribute("href")
        if href and href.startswith("http"):
            try:
                response =requests.get(href)
                if response.status_code == 400 or response.status_code == 500:
                    print(f"Broken link {href}: Status Code {response.status_code}")
                else:
                    print(f"Valid link {href}: Status Code {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(e)