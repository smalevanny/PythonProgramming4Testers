from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # init contact creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.NAME, "submit").click()
        self.app.return_to_home_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # init deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to.alert.accept()

    def edit_first(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # init deletion
        wd.find_element(By.XPATH, "(//img[@title='Edit'])[1]").click()
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element(By.NAME, "update").click()
        self.app.return_to_home_page()

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements(By.XPATH, "//input[@value='Delete']")) > 0):
            wd.find_element(By.LINK_TEXT, "home").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field("firstname",  contact.firstname)
        self.change_field("middlename", contact.middlename)
        self.change_field("lastname",   contact.lastname)
        self.change_field("nickname",   contact.nickname)
        self.change_field("title",      contact.title)
        self.change_field("company",    contact.company)
        self.change_field("address",    contact.address)
        self.change_field("home",       contact.homenumber)
        self.change_field("mobile",     contact.mobilenumber)
        self.change_field("work",       contact.worknumber)
        self.change_field("fax",        contact.faxnumber)
        self.change_field("email",      contact.email)
        self.change_field("email2",     contact.email2)
        self.change_field("email3",     contact.email3)
        self.change_field("homepage",   contact.homepage)
        self.change_field("bday",       contact.bday)
        self.change_field("bmonth",     contact.bmonth)
        self.change_field("byear",      contact.byear)
        self.change_field("aday",       contact.aday)
        self.change_field("amonth",     contact.amonth)
        self.change_field("ayear",      contact.ayear)
        self.change_field("address2",   contact.address2)
        self.change_field("phone2",     contact.phone2)
        self.change_field("notes",      contact.notes)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            if field_name in ["bday", "bmonth", "aday", "amonth"]:
                Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)
            else:
                wd.find_element(By.NAME, field_name).clear()
                wd.find_element(By.NAME, field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contacts_page()
        contacts = []
        for element in wd.find_elements(By.XPATH, "//tr[@name='entry']"):
            id = element.find_element(By.NAME, "selected[]").get_attribute("id")
            lastname_text = element.find_element(By.XPATH, "td[2]").text
            firstname_text = element.find_element(By.XPATH, "td[3]").text
            contacts.append(Contact(firstname=firstname_text, lastname=lastname_text, id=id))
        return contacts