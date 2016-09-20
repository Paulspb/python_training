# lesson 5.5 from selenium.webdriver.firefox.webdriver import WebDriver
from selenium  import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self, browser ="firefox"):
        if browser =='firefox':
            # lesson 5.5 self.wd = WebDriver()
            self.wd = webdriver.Firefox()
        elif browser =='chrom':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s " % browser)

            # lesson 3_5 self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group   = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def change_field_input(self, field_name, text):
        wd = self.wd
                # if not group.name  is None:
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
