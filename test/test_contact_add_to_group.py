# -*- coding: utf-8 -*-
from model.contact import Contact
import random

# after less 7.8
#
def test_add_contact_to_group(app,db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="add_name1"))
    old_contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact_random = random.choice(old_contacts)
        # take existing contact and just add into group
    app.contact.add_to_one_group(contact_random, groups)  # new
        # less 7.3 assert len(old_contacts) + 1 == app.contact.count()
        # less 7.3 new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
        # no need for remove old_contact as assert not verify of -group-
    assert sorted(old_contacts,key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)