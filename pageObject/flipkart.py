import time

from playwright.sync_api import expect
import logging

# from requests.packages import target

from collections import OrderedDict
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class flipkartHome:

    def __init__(self,page):
        self.page=page
        self.search_bar = "xpath=//input[@type='text']"
        self.search_bar_click = "xpath=//button[@type='submit']"
        self.login_popup = "xpath=//a[@href='/account/login?ret=/'][text()='Login']"
        self.electronics = "xpath=//span[contains(text(),'Electronics')]"
        self.mobile_device_list = "xpath=//div[contains(@data-id,'MOB')]"
        self.mobile_rows_from_list_after_model_search = "xpath=//div[contains(@class,'yKfJKb')]"

    ## >>>> Without Filters using simple for loop logic <<<<<<< ##

    def flipkart_get_mobile_price_with_mobile_name(self, desired_phone):
        expect(self.page.locator(self.login_popup)).to_be_hidden(timeout=30000)
        self.page.locator(self.search_bar).fill("mi phone")
        self.page.locator(self.search_bar_click).click()
        self.page.wait_for_selector(self.mobile_rows_from_list_after_model_search, timeout=10000)
        expect(self.page.locator(self.mobile_rows_from_list_after_model_search).first).to_be_visible(timeout=10000)
        rows = self.page.locator(self.mobile_rows_from_list_after_model_search).all()
        time.sleep(5)
        for row in rows:
            row.scroll_into_view_if_needed()
            expect(row).to_be_visible(timeout=5000)
            mobile_name = row.text_content()

            if desired_phone in mobile_name:
                price_locator = row.locator("xpath=.//div[starts-with(text(),'₹')]").first
                price = price_locator.text_content().strip()

                logger.info(f"Phone: {mobile_name} | Price: {price}")
                break

    def flipkart_mobile_name_price_in_ascending_order(self, desired_phone):
        expect(self.page.locator(self.login_popup)).to_be_hidden(timeout=30000)
        self.page.locator(self.search_bar).fill("mi phone")
        self.page.locator(self.search_bar_click).click()
        self.page.wait_for_selector(self.mobile_rows_from_list_after_model_search, timeout=10000)
        expect(self.page.locator(self.mobile_rows_from_list_after_model_search).first).to_be_visible(timeout=10000)

        rows = self.page.locator(self.mobile_rows_from_list_after_model_search).all()
        time.sleep(5)
        mobile_names = {}
        for row in rows:
            mobile_name = row.inner_text()
            row.scroll_into_view_if_needed()
            expect(row).to_be_visible(timeout=10000)
            price_locator = row.locator("xpath=/child::div[2]//div[@class='Nx9bqj _4b5DiR']")
            time.sleep(2)
            price = price_locator.text_content().strip()
            mobile_names[mobile_name] = price

        sorted_price =  sorted(mobile_names.items(), key = lambda x: int(x[1].replace("₹", "").replace(",", "").strip()))
        ordered_items = OrderedDict(sorted_price)
        sorted_lst = []
        for key,values in ordered_items.items():
            sorted_lst.append([key,values])
        print(sorted_lst)
    ## >>>> Using Filters <<<<<<< ##
    # def flipkart_get_mobile_price_with_mobile_name(self, desired_phone):
    #     expect(self.page.locator(self.login_popup)).to_be_hidden(timeout=30000)
    #     self.page.locator(self.search_bar).fill("mi phone")
    #     self.page.locator(self.search_bar_click).click()
    #     self.page.wait_for_selector(self.mobile_rows_from_list_after_model_search, timeout=10000)
    #     expect(self.page.locator(self.mobile_rows_from_list_after_model_search).first).to_be_visible(timeout=10000)
    #     rows = self.page.locator(self.mobile_rows_from_list_after_model_search)
    #     time.sleep(5)
    #     filtered_row = rows.filter(has_text=desired_phone)
    #     if filtered_row.count()>0:
    #         target_row = filtered_row.first
    #         actual_mobile_name = filtered_row.first.text_content().strip()
    #         expect(target_row).to_contain_text(desired_phone)
    #         price_locator = target_row.locator("xpath=.//div[starts-with(text(),'₹')]").first
    #         price = price_locator.text_content().strip()
    #         logger.info(f"Phone: {actual_mobile_name} | Price: {price}")
    #     else:
    #         logger.warning(f"Mobile '{desired_phone}' not found in the list.")
