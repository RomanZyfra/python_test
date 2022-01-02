from model.contacts import Contacts
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.contacts.create_contacts(Contacts(firstname="Test", middlename="Test", lastname="test", nickname="test",
                                 title="test", company="test", address="test", home="55555", mobile="777777"))
    app.session.logout()
