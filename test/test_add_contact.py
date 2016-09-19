# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_String(prefix,maxlen):
    symbol = string.ascii_letters + string.digits + " " *10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="first2name", lastName="Last2name", midName="Mid2name", nickName="nick2name",
                    companyName="company12", address1="address112", telHome="homet2", telMobile="mobileT2",
                    telWork="wrokT2")] + [
            Contact(firstname=random_String("first_name",10), lastName=random_String("Last_name",20),
                               companyName=random_String("company1",20), address1=random_String("address11",20),
                                telHome=random_String("homet",20), telMobile=random_String("mobileT",10),telWork=random_String("wrokT",10),
                                email_1=random_String("email11",10), email_2=random_String("email2",10), email_3=random_String("email3",10),
                                home_2=random_String("home2",10))
            for i in range (6)
]



#testdata = [Group(name="", header="", footer="")] + [
#      Group(name=random_String("name",10),header=random_String("header",20),footer=random_String("footer",15))
#    for i in range(5)
#      # this is 5 time for random  + one 'empty'
#


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata ])
def test_add_contact(app,contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts,key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)

