# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login( username="admin", password="secret")
    app.create_contact(Contact(firstname="first_name", lastName="Last_name", midName="Mid_name", nickName="nick_name",
                            companyName="company1", address1="address11", telHome="homet", telMobile="mobileT",
                            telWork="wrokT", fax="fas", email_1="email11", email_2="email2", email_3="email3",
                            address_2="address2", home_2="home2", note_2="note2", home_page="homePage"))
    app.logout()

