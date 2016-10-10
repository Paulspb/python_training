import mysql.connector
    #after pip install mysql-connector-python-rf
    # both driver does DB API 2.0
connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
print("------------------- after pip install mysql-connector-python-rf")
try:
    cursor = connection.cursor()
        # cursor point on place into database from http: localhost/phpmyadmin/sql.php?db......
    cursor.execute("select * from group_list")
        # then doing on whole lines
    for row in cursor.fetchall():
        print(row)
finally:
     connection.close()

# there is alternative way to connec to dabase it calls -pymysql-
import pymysql.cursors
    #after pip install PyMySQL
    #connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
print("------------------- after pip install pip install PyMySQL------------------")
try:
    cursor = connection.cursor()
        # cursor point on place into database from http: localhost/phpmyadmin/sql.php?db......
    cursor.execute("select * from group_list")
        # then doing on whole lines
    for row in cursor.fetchall():
        print(row)
finally:
     pass
     #connection.close()

print("------------------- after pip install pip install PyMySQL   addressbook DB------------------")
try:
    cursor = connection.cursor()
        # cursor point on place into database from http: localhost/phpmyadmin/sql.php?db......
    cursor.execute(
        "select id, firstname, lastname , nickname, company, "
        "title, address, home, mobile, work, fax , email, email2, email3, address2, phone2, notes "
        " from addressbook where deprecated = '0000-00-00' ")
        # then doing on whole lines
    for row in cursor.fetchall():
        print(row)
finally:
     connection.close()


#---------- less 7.7
from fixture.orm import ORMFixture
print("------------------- after pip install pony less 7.7------------------")
#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_group_list()

    for item in l:
        print(item)
    print(len(l))
finally:
     pass
