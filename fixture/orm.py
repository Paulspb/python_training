from pony.orm import *
from datetime import datetime

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
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
            # here doing the relation
        self.db.generate_mapping()

    @db_session
    def get_group_list(self):
            # take data from DB via =pony-
            #select(g for g in ORMFixture.ORMGroup)
            #convert SQL to spisok
        return list(select(g for g in ORMFixture.ORMGroup))







