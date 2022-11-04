import re

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
        self.contacts_cache = None

    def delete_first(self):
        self.delete(0)

    def delete(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact(index)
        # init deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to.alert.accept()
        self.contacts_cache = None

    def edit_first(self, contact):
        self.edit(0)

    def edit(self, index, contact):
        wd = self.open_edit_form(index)
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element(By.NAME, "update").click()
        self.app.return_to_home_page()
        self.contacts_cache = None

    def open_edit_form(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact(index)
        # init edition
        wd.find_elements(By.XPATH, "//img[@title='Edit']")[index].click()
        return wd

    def open_view_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact(index)
        # open view page
        wd.find_elements(By.XPATH, "//img[@title='Details']")[index].click()
        return wd

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

    def select_first_contact(self):
        self.select_contact(0)

    def select_contact(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contacts_cache = []
            for row in wd.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("id")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                email = cells[4].find_elements(By.TAG_NAME, "a")[0].text
                email2 = cells[4].find_elements(By.TAG_NAME, "a")[1].text
                email3 = cells[4].find_elements(By.TAG_NAME, "a")[2].text
                emails = "\n".join([email, email2, email3])
                phones = cells[5].text
                self.contacts_cache.append(Contact(firstname=firstname,
                                                   lastname=lastname,
                                                   address=address,
                                                   emails_from_home_page=emails,
                                                   phones_from_home_page=phones,
                                                   id=id))
        return list(self.contacts_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_form(index)
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        middlename = wd.find_element(By.NAME, "middlename").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        nickname = wd.find_element(By.NAME, "nickname").get_attribute("value")
        title = wd.find_element(By.NAME, "title").get_attribute("value")
        company = wd.find_element(By.NAME, "company").get_attribute("value")
        address = wd.find_element(By.NAME, "address").text
        homenumber = wd.find_element(By.NAME, "home").get_attribute("value")
        mobilenumber = wd.find_element(By.NAME, "mobile").get_attribute("value")
        worknumber = wd.find_element(By.NAME, "work").get_attribute("value")
        faxnumber = wd.find_element(By.NAME, "fax").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        homepage = wd.find_element(By.NAME, "homepage").get_attribute("value")
        address2 = wd.find_element(By.NAME, "address2").text
        phone2 = wd.find_element(By.NAME, "phone2").get_attribute("value")
        notes = wd.find_element(By.NAME, "notes").text
        return Contact(firstname=firstname,
                       middlename=middlename,
                       lastname=lastname,
                       nickname=nickname,
                       title=title,
                       company=company,
                       address=address,
                       homenumber=homenumber,
                       mobilenumber=mobilenumber,
                       worknumber=worknumber,
                       faxnumber=faxnumber,
                       email=email,
                       email2=email2,
                       email3=email3,
                       homepage=homepage,
                       address2=address2,
                       phone2=phone2,
                       notes=notes,
                       id=id)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_page(index)
        text = wd.find_element(By.ID, "content").text
        homenumber = re.search("H: (.*)", text).group(1)
        mobilenumber = re.search("M: (.*)", text).group(1)
        worknumber = re.search("W: (.*)", text).group(1)
        faxnumber = re.search("F: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homenumber=homenumber,
                       mobilenumber=mobilenumber,
                       worknumber=worknumber,
                       faxnumber=faxnumber,
                       phone2=phone2)


