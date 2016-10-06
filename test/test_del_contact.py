from model.contact import Contact
import random

def test_delete_some_contact(app, db,check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(firstname="add_name1"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
        #index = randrange(len(old_contacts))
        #les 7.4app.contact.delete_contact_by_id(contact.id)
    app.contact.delete_contact_by_id(int(contact.id))
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
        #old_contacts[index:index+1] = []
    old_contacts.remove(contact)
    assert len(old_contacts)  == len(new_contacts)
    #less 7.5
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)




