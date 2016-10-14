from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
# if c.deprecated is not valid fror SQL
from pymysql.converters import decoders
    # lesson 7.8
from pymysql.converters import encoders, decoders, convert_mysql_timestamp

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column = 'group_id')
        name = Optional(str, column = 'group_name')
        header = Optional(str, column = 'group_header')
        footer = Optional(str, column = 'group_footer')
                # less 7.8
                # we can't write directly a link on -Contact-
        contacts = Set(lambda: ORMFixture.ORMContact, table= "address_in_groups", column= "id", reverse="groups", lazy=True )

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column= 'id')
        firstName = Optional(str, column = 'firstname')
        lastName = Optional(str, column='lastname')
        deprecated = Optional(datetime, column ='deprecated')
                #less 7.8
        groups = Set(lambda: ORMFixture.ORMGroup, table= "address_in_groups", column= "group_id", reverse="contacts", lazy=True)

        # relation between definition and  real our DB
        # this is constructor
    def __init__(self, host, name, user, password):
                # if c.deprecated is not valid fror SQL
                # self.db.bind('mysql', host=host, database=name, user=user, password=password)
                # for less 7.7, not for 7.8
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        #self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
                # for less 7.8
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)

            # here doing the relation
        self.db.generate_mapping()
            #for monitoring SQL process
                # home task 22
        ###sql_debug(True)

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


#--------------- lesson 7.8 -group name- placed within -contact- ----------------------------
    @db_session # means execute within connection to DB
    def get_contact_in_group(self,group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        #orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))
                # take only first element via [0]
                # there is object called -orm_group-
        return self.convert_contacts_to_model(orm_group.contacts)




