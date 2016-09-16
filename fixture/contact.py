from model.contact import Contact

class ContactHelper:
    # constructor
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.create_names(contact.firstname, contact.lastName, contact.midName, contact.nickName,contact.title)
        self.create_company_address1( contact.address1,contact.companyName)
        self.create_telephones_fax( contact.telHome, contact.telMobile, contact.telWork, contact.fax)
        self.create_emails(contact.email_1, contact.email_2, contact.email_3)
        self.create_home_page(contact.home_page)
        self.create_dates()
        # fill-in dates2
        self.app.change_field_input("byear", "2005")
        self.create_address2_home2(contact.address_2, contact.home_2, contact.note_2)

    def create_home_page(self, home_page):
        wd = self.app.wd
        self.app.change_field_input("homepage", home_page)

    def create_dates(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()

    def create_address2_home2(self, address_2, home_2, note_2):
        wd = self.app.wd
        self.app.change_field_input("address2", address_2)
        self.app.change_field_input("phone2", home_2)
        self.app.change_field_input("notes", note_2)

    def create_emails(self, email_1, email_2, email_3):
        wd = self.app.wd
        self.app.change_field_input("email", email_1)
        self.app.change_field_input("email2", email_2)
        self.app.change_field_input("email3", email_3)

    def create_company_address1(self, address1, companyName):
        wd = self.app.wd
        self.app.change_field_input("address", address1)
        self.app.change_field_input("company", companyName)

    def create_telephones_fax(self, telHome, telMobile, telWork, fax):
        wd = self.app.wd
        self.app.change_field_input("home", telHome)
        self.app.change_field_input("mobile", telMobile)
        self.app.change_field_input("work", telWork)
        self.app.change_field_input("fax", fax)

    def create_names(self, firstname, lastNname, midName, nickName,title):
        wd = self.app.wd
        self.app.change_field_input("firstname", firstname)
        self.app.change_field_input("middlename", midName)
        self.app.change_field_input("lastname", lastNname)
        self.app.change_field_input("nickname", nickName)
        self.app.change_field_input("title", title)

    def return_to_contact(self):
        wd = self.app.wd
        if len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img")) > 0  \
                and len(wd.find_elements_by_xpath("//div[@id='content']/form[2]/div[1]/input")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_contact()

    def modify_first_contact(self,contact):
        wd = self.app.wd
        self.return_to_contact()
        # open first concat for edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        #submit update
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_contact()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_contact()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.return_to_contact()

    def count(self):
        wd = self.app.wd
        self.return_to_contact()
        return len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img"))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_to_contact()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            # text = element.text()
            last_name = element.find_element_by_xpath(".//td[2]").text
            first_name = element.find_element_by_xpath(".//td[3]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(lastName=last_name, id=id, firstname=first_name))
        return contacts

