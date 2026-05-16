# import pytest
# from pytest_playwright.pytest_playwright import browser, playwright, context

# from pageObject.flipkart import *
# from playwright.sync_api import Page

# from utilities.base_class_utils import BaseClass

# @pytest.mark.usefixtures("start_browser_with_tracing")
# def test_flipkart_aut(start_browser_with_tracing):
#     page = start_browser_with_tracing
#     base = BaseClass(page)
#     base.go_to_url("https://www.flipkart.com/")
#     flipkart = flipkartHome(page)
#     flipkart.flipkart_get_mobile_price_with_mobile_name("Redmi 5A (Blue, 16 GB)")


# def test_product_name_price_sorted(start_browser_with_tracing):
#     page = start_browser_with_tracing
#     base = BaseClass(page)
#     base.go_to_url("https://www.flipkart.com")
#     flipkart = flipkartHome(page)
#     flipkart.flipkart_mobile_name_price_in_ascending_order("Redmi 5A (Blue, 16 GB)")
