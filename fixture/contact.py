from model.contact import Contact
import re
class ContactHelper:
    # constructor
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if len(wd.find_elements_by_name("photo")) > 0  \
                and len(wd.find_elements_by_name("amonth")) > 0:
            return
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
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self,index,contact):
        wd = self.app.wd
        self.return_to_contact()
        self.select_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        #submit update
            # wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        wd.find_element_by_name("update").click()
        self.return_to_contact()
        self.contact_cache = None

    def select_contact_to_edit_by_index(self, index):
        wd = self.app.wd
            # open index element - my version based on recorder
        #wd.find_elements_by_name("selected[]")[index].click()
        #ind = str(index +2)
        #wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr["+ind+"]/td[8]/a/img").click()
            # other version from lesson 5_2
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        ##cell.find_element_by_name("a").click()  <-- not valid !!!! remember
        cell.find_element_by_tag_name("a").click()


    def select_contact_to_view_by_index(self,index):
        wd = self.app.wd
            # other version from lesson 5_2
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        ##cell.find_element_by_name("a").click()  <-- not valid !!!! remember
        cell.find_element_by_tag_name("a").click()


    def get_contact_from_info_from_edit_page(self,index):
        wd = self.app.wd
        self.select_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        # home task 14
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname = firstname, lastName = lastname, id= id,
            telHome = homephone, telMobile = mobilephone, telWork = workphone, home_2 = phone2,
                       email_1=email1,email_2=email2,email_3=email3,address1=address)

    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.select_contact_to_view_by_index(index)
        text =wd.find_element_by_id("content").text
        if re.search("H: (.*)", text) is not None:
            homephone = re.search("H: (.*)",text).group(1)
        else:
            homephone = ''

        if re.search("W: (.*)", text) is not None:
            workphone = re.search("W: (.*)", text).group(1)
        else:
            workphone = ''

        if re.search("M: (.*)", text) is not None:
            mobilephone = re.search("M: (.*)", text).group(1)
        else:
            mobilephone = ''

        if re.search("P: (.*)", text) is not None:
            phone2 = re.search("P: (.*)", text).group(1)
        else:
            phone2 = ''

        self.return_to_contact()
        return Contact(telHome=homephone, telMobile=mobilephone, telWork=workphone, home_2=phone2)



    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.return_to_contact()
        self.select_contact_to_edit_by_index(index)
        #wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.return_to_contact()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.return_to_contact()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        #home task 14
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_contact()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                # text = element.text()
                    # cells = row.find_elements_by_tag_name("td")
                    # firstname = cell[1].text
                last_name = element.find_element_by_xpath(".//td[2]").text
                first_name = element.find_element_by_xpath(".//td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                # less 5.3 all_phones = element.find_element_by_xpath(".//td[6]").text.splitlines()
                all_phones  = element.find_element_by_xpath(".//td[6]").text
                # home task 14
                all_emails  = element.find_element_by_xpath(".//td[5]").text
                full_address = element.find_element_by_xpath(".//td[4]").text

                self.contact_cache.append(Contact(lastName=last_name, id=id, firstname=first_name,address1=full_address,
                        all_phones_from_home_page= all_phones, all_emails_from_home_page=all_emails))
                        # less 5.3 telHome= all_phones[0],telMobile=all_phones[1], telWork = all_phones[2],home_2=all_phones[3]))
        return self.contact_cache

