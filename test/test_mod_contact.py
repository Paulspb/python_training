from model.contact import Contact

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="add_name1"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(
             firstname="first_name_mod1231", lastName="Last_name_mod1", midName="Mid_name", nickName="nick_name",
             title= "Mr",companyName="company1", address1="address11", telHome="homet", telMobile="mobileT",
             telWork="wrokT", fax="fas", email_1="email11", email_2="email2", email_3="email3",
             address_2="address2", home_2="home2", note_2="note2", home_page="homePage"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="add_name1"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(
             firstname="first_name_mod1Name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="add_name1"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(
             lastName="Last_name_mod1LastName"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
