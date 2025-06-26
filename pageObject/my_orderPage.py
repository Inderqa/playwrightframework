from pageObject.order_Summary import order_summary


class my_orders:

    def __init__(self,page):
        self.page = page

    def order_history_view(self):
        row = self.page.locator("//tr[@class='ng-star-inserted']").nth(0)
        view_button = row.locator("//button[contains(text(), 'View')]")
        view_button.click()
        order_details = order_summary(self.page)
        return order_details
