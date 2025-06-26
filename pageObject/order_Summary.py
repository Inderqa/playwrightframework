from playwright.sync_api import expect
class order_summary:

    def __init__(self,page):
        self.page = page

    def order_complete_text(self):
        expect(self.page.locator("//p[@class='tagline']")).to_contain_text("Thank you for Shopping With Us")