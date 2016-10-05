# -*- coding: utf-8 -*-
from model.contact import Contact
    #import pytest
    #from data.add_contact import testdata
    #from data.contacts import constant as testdata

        #testdata = [Group(name="", header="", footer="")] + [
        #      Group(name=random_String("name",10),header=random_String("header",20),footer=random_String("footer",15))
        #    for i in range(5)
        #      # this is 5 time for random  + one 'empty'

# -revoke- lesson 6.5 @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata ])
# less 6.5 def test_add_contact(app,contact): -> join with data/contacts.py file
#
def test_add_contact(app,db,json_contacts):
    contact = json_contacts
    # less 7.3 old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    # less 7.3 new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts,key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)

