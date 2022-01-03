from model.contact import Contact


def test_edit_first_contact(app):
    app.contacts.edit_first_contact(Contact(firstname="Test1", middlename="Test1", lastname="test1", nickname="test1",
                                            title="test1", company="test1", address="test1", home="555551", mobile="7777771"))

