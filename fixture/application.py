# lesson 5.5 from selenium.webdriver.firefox.webdriver import WebDriver
from selenium  import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
    #--home task 22
#from fixture.orm import ORMFixture

class Application:

    #-revoke- less 5.5 def __init__(self, browser ="firefox"):
    def __init__(self, browser, base_url):
        if browser =='firefox':
            # lesson 5.5 self.wd = WebDriver()
            self.wd = webdriver.Firefox()
        # elif browser =='chrom': sep 28
        elif browser =='chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s " % browser)

            # lesson 3_5 self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group   = GroupHelper(self)
        self.contact = ContactHelper(self)
            # -add- less 5.5
        self.base_url = base_url
            # home task 22
        #self.orm = ORMFixture(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
            #-revoke- less 5.5
            # wd.get("http://localhost/addressbook/")
        wd.get("http://localhost/addressbook/")
            # not work after 7.1
        #wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def change_field_input(self, field_name, text):
        wd = self.wd
                # if not group.name  is None:
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
