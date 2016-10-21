from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

import re
class ContactHelper:
    # constructor
    def __init__(self, app):
        self.app = app
        #self.orm = orm
            #-- home task 22
        #self.orm = orm
        # self.db = db

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

    def add_to_one_group(self, contact, groups, orm):
        wd = self.app.wd
        self.return_to_contact()
            #new_group = self.select_one_group(contact, groups, "add")
        new_group = orm.select_one_group(contact, groups, "add")
            #print(contact.id, contact.firstname, contact.lastName, new_group)
        if new_group.name == "xxx":
            print("!!! all groups is already added to contact : 'first name' =" + contact.firstname)
        else:
            self.adding_one_group(contact.id, new_group, groups)
            self.contact_cache = None
        return new_group  # oct,19 22-00

    def remove_from_one_group(self, contact, groups, orm):
        wd = self.app.wd
        self.return_to_contact()
        new_group = orm.select_one_group(contact, groups, "remove")
            #print(contact.id, contact.firstname, contact.lastName, new_group)
        if new_group.name == "xxx":
            print("!!!!!!!! no any group asssigned for this contact : 'first name' ="
                  + contact.firstname + "   'last name = " +contact.lastName)
        else:
            self.delete_from_one_group(contact.id, new_group, groups)
            self.contact_cache = None
        return new_group  # oct,19 22-00


    def get_groups_in_contact(self,contact):
        #dborm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
        orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
        l2 =3
        #orm = self.orm
        try:
            l = orm.get_group_in_contact(Contact(id=str(contact.id)))
            for item in l:
                print(item)
            print(len(l))
        finally:
            pass
        return l

    def select_one_group(self, contact, groups, moving):
        #dborm  = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
        #TypeError: Database object was already bound to MySQL provider
        #orm = self.orm
        wd = self.app.wd

            # create temp_group list  with whole names of group
        temp_group = []
        new_group_name = "xxx"
            # movement = 'add' or 'remove'
            ## fill-in temporary groups  with mark   '111'
        for group1 in groups:
           temp_group.append(Group(id=str(group1.id), name=group1.name, header = 111, footer=group1))

        #print(contact.id, contact.firstname, contact.lastName)
        #for y in temp_group:
        ##   print(y.name, y.id, y.header, y.footer)


        for element in temp_group:
                # group_id is not 0
            if element.id != 0:
                try:
                    #l1 = dborm.get_contact_in_group(Group(id=str(element.id)))
                    l1 = orm.get_contact_in_group(Group(id=str(element.id)))
                    #get_contact_in_group
                        #if group ralated with any contact
                    if len(l1) != 0:
                        for item in l1:
                            #print(item)
                                # if the contact present into this group, then marks as 0
                            if item.id == contact.id:
                                element.header = 0

                        #print(len(l1))
                finally:
                    pass

                #init value
        choice = 2
        if moving == "add":
            choice = 111

        if moving == "remove":
            choice = 0

            # read first group marked as '111' for add (still not used in contact)
            # read first group marked as '0' for remove (still not used in contact)

        for one_group in temp_group:
            if one_group.header == choice:
                if choice == 111:
                    print(" *********** this group adding:  " + one_group.id + " " + one_group.name)
                if choice == 0:
                    print(" *********** this group removing:  " + one_group.id + " " + one_group.name)
            return  one_group.name

        return new_group_name



    #-  home 22 ----------------------------------------------------
    def adding_one_group(self, contact_id, new_group, groups):
        wd = self.app.wd
            # select adding group by -new_group-
        if len(wd.find_elements_by_name("to_group")) > 0:
                # not work wd.find_element_by_xpath("//select[@name='to_group']/option[text()='%s']" % new_group).click
            el = wd.find_element_by_xpath("//select[@name='to_group']")
            if len(el.find_elements_by_tag_name('option')) > 0:
                i1 = 0
                groups_sorted = sorted(groups, key=lambda Group: Group.name)
                for option in el.find_elements_by_tag_name('option'):
                        # if group_name is the same for several groups
                    if option.text == new_group.name:
                        if groups_sorted[i1].id == new_group.id:
                            option.click()
                            break
                    #if len(option.text) > 0:
                    i1 = i1 + 1

            #not work wd.find_element_by_xpath("//select[@name='group']/option[text()='[all]']").click
            el = wd.find_element_by_xpath("//select[@name='group']")
            for option in el.find_elements_by_tag_name('option'):
                if option.text == '[all]':
                    option.click()
                    break

            # if the contact is still available, tehn click on contact for adding
        if len(wd.find_elements_by_name("selected[]")) > 0:
            wd.find_element_by_css_selector("input[value='" + contact_id + "']").click()
            wd.find_element_by_css_selector("input[value='Add to']").click()

        self.return_to_contact()


    def delete_from_one_group(self, contact_id, new_group, groups):
        wd = self.app.wd
            # select deleting group by -new_group-
        if len(wd.find_elements_by_name("group")) > 0:
            el = wd.find_element_by_xpath("//select[@name='group']")
                #i1 = 0
                #groups_sorted = sorted(groups, key=lambda Group: Group.name)
            for option in el.find_elements_by_tag_name('option'):
                if option.text == new_group.name:
                #    if groups_sorted[i1].id == new_group.id:
                        option.click()
                        break
                #if option.text != "[all]" and option.text != "[none]" :
                #    i1 = i1 + 1

            # if the contact is still available, tehn click on contact for adding
        if len(wd.find_elements_by_name("selected[]")) > 0:
            wd.find_element_by_css_selector("input[value='" + contact_id + "']").click()
            wd.find_element_by_css_selector("input[name='remove']").click()

        self.return_to_contact()
            # return default value [all]
        el = wd.find_element_by_xpath("//select[@name='group']")
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '[all]':
                option.click()
                break


    #--------------------------------------

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

        #home 20
    def modify_contact_by_id(self,contact_id,contact):
        wd = self.app.wd
        self.return_to_contact()
        self.select_contact_to_edit_by_id(contact_id)
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

        # less 7.4
    def select_contact_to_edit_by_id(self, id):
        wd = self.app.wd
                #less 7.4, home #20
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()


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

    def delete_contact_by_id(self,id):
        wd = self.app.wd
        self.return_to_contact()
        self.select_contact_to_edit_by_id(id)
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

