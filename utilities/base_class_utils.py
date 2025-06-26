import logging

import pytest
from playwright.async_api import Expect
from playwright.sync_api import Page, expect


@pytest.mark.usefixtures("start_browser")
class BaseClass:
    def __init__(self,page):
        self.page =page

    def get_title(self):
        return self.page.title

    def generic_xpath(self,tag_name,variable):
        return self.page.locator("//{}[contains(normalize-space(text()), '{}')]".format(tag_name, variable))

    def generic_xpath_at_rate(self,tag_name,attribute,variable):
        return self.page.locator("//{}[@{}='{}']".format(tag_name, attribute,variable))

    def go_to_url(self,url):
        self.page.goto(url)

