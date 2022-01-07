from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.contacts.open_contact_page()
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname="Test"))
    app.contacts.modify_first_contact(Contact(firstname="New Test"))


def test_modify_first_contact_middlename(app):
    app.contacts.open_contact_page()
    if app.contacts.count() == 0:
        app.contacts.create(Contact(middlename="New Test"))
    app.contacts.modify_first_contact(Contact(middlename="New Test"))
