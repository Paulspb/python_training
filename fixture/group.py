from model.group import Group

class GroupHelper:
    # constructor
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
                # if not group.name  is None:
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        #self.change_field_value("group_name", group.name)
        self.app.change_field_input("group_name", group.name)
        self.app.change_field_input("group_header", group.header)
        self.app.change_field_input("group_footer", group.footer)

    def return_to_groups_page(self):
        wd = self.app.wd
        # update for home task 10
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    # lesson 4.5 def modify_first_group(self,new_group_data):
    def modify_first_group(self,new_group_data):
        self.modify_group_by_index(0,new_group_data)

    def modify_group_by_index(self,index,new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #modification
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        #submit updation
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_id(self,group_id,new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(group_id)
        #modification
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        #submit updation
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self,index):
        wd = self.app.wd
        # less 4.5 wd.find_element_by_name("selected[]").click()
        wd.find_elements_by_name("selected[]")[index].click()

        # less 7.4
    def select_group_by_id(self,id):
        wd = self.app.wd
        # less 4.5 wd.find_element_by_name("selected[]").click()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        ##wd.findElement(By.cssSelector("input[value='" + id + "']")).click();

    def delete_first_group(self):
        self.delete_group_by_index(0)
            # lesson 4.5
        #wd = self.app.wd
        #self.select_first_group()
        ##submit delition
        #wd.find_element_by_name("delete").click()
        #self.return_to_groups_page()
        #self.group_cache = None

    def delete_group_by_index(self,index):
        wd = self.app.wd
        self.open_groups_page()
            # less 4.5self.select_first_group()
        self.select_group_by_index(index)
        #submit delition
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self,id):
        wd = self.app.wd
        self.open_groups_page()
            # less 4.5self.select_first_group()
        self.select_group_by_id(id)
        #submit delition
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return  len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text,id=id))
        return list(self.group_cache)
