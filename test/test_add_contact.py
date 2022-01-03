from model.contact import Contact


def test_add_contact(app):
    app.contacts.create(Contact(firstname="Test", middlename="Test", lastname="test", nickname="test",
                                title="test", company="test", address="test", home="55555", mobile="777777"))

