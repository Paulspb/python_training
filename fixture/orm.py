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


#--------- home task 22 ----------------------------------------------------------------------
    def destroy(self):
        self.db.disconnect

    @db_session # means execute within connection to DB
    def get_group_in_contact(self,contact):
        orm_group = list(select(g for g in ORMFixture.ORMContact if g.id == contact.id))[0]
        #orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == contact.id))[0]

                # take only first element via [0]
                # there is object called -orm_group-
        #return self.convert_contacts_to_model(orm_group.contacts)
        return self.convert_groups_to_model(orm_group.groups)


    def get_groups_in_contact(self,contact):
        print("\n")
        try:
            l = self.get_group_in_contact(Contact(id=str(contact.id)))
            for item in l:
                print(item)
            print(len(l))
        finally:
            pass
        return l

#----------------------------------------------------------------------------------------------
    def select_one_group(self, contact, groups, moving):
            # create temp_group list  with whole names of group
        temp_group = []
        new_group_name = "xxx"
            # movement = 'add' or 'remove'
            ## fill-in temporary groups  with mark   '111'
        for group1 in groups:
           temp_group.append(Group(id=str(group1.id), name=group1.name, header = 111))

        #print(contact.id, contact.firstname, contact.lastName)
        #for y in temp_group:
        ##   print(y.name, y.id, y.header, y.footer)


        for element in temp_group:
                # group_id is not 0
            if element.id != 0:
                try:
                    l1 = self.get_contact_in_group(Group(id=str(element.id)))
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
                return  one_group

        return new_group_name





