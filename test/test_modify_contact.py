from model.contact import Contact


def test_modify_first_contact_firstname(app):
    app.contacts.modify_first_contact(Contact(firstname="New Test"))


def test_modify_first_contact_middlename(app):
    app.contacts.modify_first_contact(Contact(middlename="New Test"))
