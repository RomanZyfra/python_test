from model.contact import Contact


def test_delete_first_contacts(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname="Test"))
    app.contacts.delete_first_contact()
