from model.contacts import Contacts


def test_add_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contacts.create(Contacts(firstname="Test", middlename="Test", lastname="test", nickname="test",
                                 title="test", company="test", address="test", home="55555", mobile="777777"))
    app.session.logout()
