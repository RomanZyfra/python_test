class ContactsHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contacts):
        wd = self.app.wd
        # init contacts creation
        wd.find_element_by_link_text("add new").click()
        # fill contacts form
        self.fill_contact_form(contacts)
        # submit contacts creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def edit_first_contact(self, contacts):
        wd = self.app.wd
        # select first contacts
        wd.find_element_by_name("selected[]").click()
        # submit edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contacts form
        self.fill_contact_form(contacts)
        # submit contacts edit
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def fill_contact_form(self, contacts):
        wd = self.app.wd
        self.change_value("firstname", contacts.firstname)
        self.change_value("middlename", contacts.middlename)
        self.change_value("lastname", contacts.lastname)
        self.change_value("nickname", contacts.nickname)
        self.change_value("title", contacts.title)
        self.change_value("company", contacts.company)
        self.change_value("address", contacts.address)
        self.change_value("home", contacts.home)
        self.change_value("mobile", contacts.mobile)

    def change_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contacts
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, new_contacts_data):
        wd = self.app.wd
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contacts form
        self.fill_contact_form(new_contacts_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
