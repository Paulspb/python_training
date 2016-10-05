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
     connection.close()

