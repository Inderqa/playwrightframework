from pageObject.dashboard import dashboard


class loginpage:

    def __init__(self,page):
        self.page = page

    def navigation(self,url):
        self.page.goto(url)

    def login(self,user_email,user_password):
        self.page.locator("//input[@type='email']").fill(user_email)
        self.page.locator("//input[@type='password']").fill(user_password)
        self.page.locator("//input[@name='login']").click()
        dashboard_page = dashboard(self.page)
        return dashboard_page

