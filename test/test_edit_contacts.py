from model.contacts import Contacts


def test_edit_first_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contacts.edit_first_contacts(Contacts(firstname="Test1", middlename="Test1", lastname="test1", nickname="test1",
                                              title="test1", company="test1", address="test1", home="555551", mobile="7777771"))
    app.session.logout()
