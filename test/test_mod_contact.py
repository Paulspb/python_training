from model.contact import Contact
from random import randrange
import random

def test_modify_first_contact(app,db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="add_name1"))
    old_contacts = app.contact.get_contact_list()
            #less 7.4 index = randrange(len(old_contacts))
    contact_random = random.choice(old_contacts)
    contact = Contact(firstname="first_name", lastName="Last_name", midName="Mid_name", nickName="nick_name",
                      companyName="company1", address1="address11", telHome="1234", telMobile="456",
                      telWork="789", fax="fas", email_1="email11", email_2="email2", email_3="email3",
                      address_2="address2", home_2="00012", note_2="note2", home_page="homePage")
            #less 7.4contact.id = old_contacts[index].id
    contact.id = contact_random.id
        #contact.address1 = index
        #app.contact.modify_contact_by_index(index,contact)
    app.contact.modify_contact_by_id(contact_random.id, contact)
    new_contacts = app.contact.get_contact_list()
        #home 20
    old_contacts.remove(contact_random)
    old_contacts.append(contact)
        #assert len(old_contacts) == len(new_contacts)
        # old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="add_name1"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(
             firstname="first_name_mod1Name")
    contact.id = old_contacts[index].id
    contact.address1 = index
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    #old_contacts[index] = contact
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="add_name1"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact  = Contact(
             lastName="Last_name_mod1LastName")
    contact.id = old_contacts[index].id
    contact.address1 = index
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    #old_contacts[index] = contact
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
