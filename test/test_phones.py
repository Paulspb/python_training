import re
from random import randrange
from model.contact import Contact

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page =  app.contact.get_contact_from_info_from_edit_page(0)
        # lesson 5.3
        #assert contact_from_home_page.telHome   == clear(contact_from_edit_page.telHome)
        #assert contact_from_home_page.telMobile == clear(contact_from_edit_page.telMobile)
        #assert contact_from_home_page.telWork   == clear(contact_from_edit_page.telWork)
        #assert contact_from_home_page.home_2    == clear(contact_from_edit_page.home_2)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_from_info_from_edit_page(0)
    assert contact_from_view_page.telHome   == contact_from_edit_page.telHome
    assert contact_from_view_page.telMobile == contact_from_edit_page.telMobile
    assert contact_from_view_page.telWork == contact_from_edit_page.telWork
    assert contact_from_view_page.home_2  == contact_from_edit_page.home_2

    # home task 14
def test_home_page_vs_edit_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="add_name1"))
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list() [index]
    contact_from_edit_page = app.contact.get_contact_from_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastName == contact_from_edit_page.lastName
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert clear(contact_from_home_page.all_emails_from_home_page) == merge_emails_like_on_home_page(contact_from_edit_page)
    assert clear(contact_from_home_page.address1)                  == merge_address_like_on_home_page(contact_from_edit_page)

def clear(s):
    # what, new value, where,
    return re.sub("[() -]", "",s)

def merge_phones_like_on_home_page(contact):
    # lambda instead of clear() for each member
    #return  "\n".join(map(lambda x: clear(x), [contact.telHome,contact.telWork,contact.telMobile,contact.home_2]))
    # for aviod \n using filter
    #return "\n".join(filter(lambda x: x != "",
    #                        map(lambda x: clear(x), [contact.telHome, contact.telMobile,  contact.telWork, contact.home_2])))
    # for aviod None before clear() using filter
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter( lambda x: x is not None,
                                        [contact.telHome, contact.telMobile,  contact.telWork, contact.home_2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email_1,contact.email_2,contact.email_3]))))


def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.address1]))))


