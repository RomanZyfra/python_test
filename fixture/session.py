class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='top']/form/a").click()

    def ensure_logout(self):
        wd = self.app.wd
        self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        if wd.find_element_by_name("user") == None:
            wd.find_element_by_name("user").send_keys(username)
        if wd.find_element_by_name("pass") == None:
            wd.find_element_by_name("pass").send_keys(password)
        self.login(username, password)
