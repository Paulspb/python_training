# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact =Contact(firstname="first_name", lastName="Last_name", midName="Mid_name", nickName="nick_name",
                               companyName="company1", address1="address11", telHome="homet", telMobile="mobileT",
                               telWork="wrokT", fax="fas", email_1="email11", email_2="email2", email_3="email3",
                               address_2="address2", home_2="home2", note_2="note2", home_page="homePage")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts,key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)

