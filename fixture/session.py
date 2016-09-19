
class SessionHelper:

    #constructor
    def  __init__(self,app):
        self.app = app

    def login(self, username, password):
                # wd = self.wd
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        # les 5.1 return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"
        # less 5.1 return wd.find_element_by_xpath("//div/div[1]/form/b").text == "%s" % username
        return self.get_logged_user() == username

        # less 5.1
    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]


    def ensure_logout(self):
        wd = self.app.wd
        # if we are in ?
        if self.is_logged_in():
            self.logout()

    def ensure_login(self,username,password):
        wd = self.app.wd
        # if we are in ?
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username,password)
