# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
#from data.add_contact import testdata
from data.add_contact import constant as testdata

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

