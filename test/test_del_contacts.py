def test_delete_first_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contacts.delete_first_contacts()
    app.session.logout()
