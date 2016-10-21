# -*- coding: utf-8 -*-
from model.contact import Contact
import random

# after less 7.8
#
def test_add_contact_to_group(app,db, orm):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="add_name1"))
    old_contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact_random = random.choice(old_contacts)
        ###-works- old_groups_in_contact = app.contact.get_groups_in_contact(contact_random)

        #old_groups_in_contact = app.contact.get_groups_in_contact(contact_random)
    old_groups_in_contact = orm.get_groups_in_contact(contact_random)
        # take existing contact and just add into group
    new_group = app.contact.add_to_one_group(contact_random, groups, orm)  # new
    new_groups_in_contact = orm.get_groups_in_contact(contact_random)
    old_groups_in_contact.append(new_group)

    assert sorted(old_groups_in_contact, key=Contact.id_or_max) == sorted(new_groups_in_contact, key=Contact.id_or_max)
    new_contacts = db.get_contact_list()
        # no need for remove old_contact as assert not verify of -group-
    assert sorted(old_contacts,key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)
