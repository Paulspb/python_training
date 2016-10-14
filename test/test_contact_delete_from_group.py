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
    app.contact.remove_from_one_group(contact_random, groups)  # new
    new_contacts = db.get_contact_list()
        # no need for remove old_contact as assert not verify of -group-
    assert sorted(old_contacts,key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)
