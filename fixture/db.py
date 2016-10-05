import mysql.connector
from model.group import Group


class DbFixture:

    def __init__(self,host,name,user,password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)

    def get_group_list(self):
                # it similar group.get_group_list() !!!!!
            # create a array for return
        list = []
            # less 7.3 - not without self.    work-cursor = connection.cursor()
        cursor = self.connection.cursor()
            # cursor point on place into database from http: localhost/phpmyadmin/sql.php?db......
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
                # then doing on whole lines
            #for row in cursor.fetchall():
            for row in cursor:
                (id, name,header,footer) = row
                list.append(Group(id =str(id), name=name, header=header,footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()