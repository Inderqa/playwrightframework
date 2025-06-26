from pageObject.my_orderPage import my_orders


class dashboard:

    def __init__(self,page):
        self.page = page


    def dashboard_orders(self):
        self.page.locator("//*[contains(normalize-space(text()), 'ORDERS')]").click()
        orders_history = my_orders(self.page)
        return orders_history
