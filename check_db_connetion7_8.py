#---------- less 7.8
from fixture.orm import ORMFixture
print("------------------- lesson 7.8 SQL to -group_in_contact-   via pony ------------------")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
##db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
from model.group import Group
try:
    l = db.get_contact_in_group(Group(id="543"))

    for item in l:
        print(item)
    print(len(l))
finally:
     pass
