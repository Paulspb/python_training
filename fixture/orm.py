from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
# if c.deprecated is not valid fror SQL
from pymysql.converters import decoders

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column = 'group_id')
        name = Optional(str, column = 'group_name')
        header = Optional(str, column = 'group_header')
        footer = Optional(str, column = 'group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column= 'id')
        firstName = Optional(str, column = 'firstname')
        lastName = Optional(str, column='lastname')
        deprecated = Optional(datetime, column ='deprecated')

        # relation between definition and  real our DB
        # this is constructor
    def __init__(self, host, name, user, password):
                # if c.deprecated is not valid fror SQL
                # self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.bind('mysql', host=host, database=name, user=user, password=password,conv=decoders)

            # here doing the relation
        self.db.generate_mapping()
            #for monitoring SQL process
        sql_debug(True)

# --------------- for GROUP ----------------------------
    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id =str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
            # take data from DB via =pony-
            #select(g for g in ORMFixture.ORMGroup)
            #convert SQL to spisok
        #return list(select(g for g in ORMFixture.ORMGroup))   # return ORMGroup[547]
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

#--------------- for CONTACT ----------------------------
    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            #return Group(id =str(group.id), name=group.name, header=group.header, footer=group.footer)
            #- mnogo !!!return Contact(id =str(contact.id), firstname=contact.firstname, lastName=contact.lastname, companyName=contact.company, address1=contact.address)
            return Contact(id=str(contact.id), firstname=contact.firstName, lastName=contact.lastName)

        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
            # if in Pyton is the same as where in SQL
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))
        #return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact ))







