import random

from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    if len(db.get_contacts_list()) == 0:
        contact = Contact(firstname="firstname",
                          middlename="middlename",
                          lastname="lastname",
                          nickname="nickname",
                          title="title",
                          company="company",
                          address="address",
                          homenumber="homenumber",
                          mobilenumber="mobilenumber",
                          worknumber="worknumber",
                          faxnumber="faxnumber",
                          email="email",
                          email2="email2",
                          email3="email3",
                          homepage="homepage",
                          bday="1",
                          bmonth="January",
                          byear="1981",
                          aday="2",
                          amonth="January",
                          ayear="2000",
                          address2="address2",
                          phone2="phone2",
                          notes="notes")
        app.contact.create(contact)
    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    groups = db.get_groups_list()
    group = random.choice(groups)
    contacts_not_in_group = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts_not_in_group)
    print(contact)
    app.contact.add_to_group(contact, group)
    contacts_in_group = db.get_contacts_in_group(group)
    contacts_not_in_group = db.get_contacts_not_in_group(group)
    assert contact in contacts_in_group
    assert contact not in contacts_not_in_group

def test_delete_contact_from_group(app):
    if len(db.get_contacts_list()) == 0:
        contact = Contact(firstname="firstname",
                          middlename="middlename",
                          lastname="lastname",
                          nickname="nickname",
                          title="title",
                          company="company",
                          address="address",
                          homenumber="homenumber",
                          mobilenumber="mobilenumber",
                          worknumber="worknumber",
                          faxnumber="faxnumber",
                          email="email",
                          email2="email2",
                          email3="email3",
                          homepage="homepage",
                          bday="1",
                          bmonth="January",
                          byear="1981",
                          aday="2",
                          amonth="January",
                          ayear="2000",
                          address2="address2",
                          phone2="phone2",
                          notes="notes")
        app.contact.create(contact)
    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    contacts = db.get_contacts_list()
    groups = db.get_groups_list()
    group = random.choice(groups)
    if len(db.get_contacts_in_group(group)) == 0:
        app.contact.add_to_group(random.choice(contacts), group)
    contact = random.choice(db.get_contacts_in_group(group))
    app.contact.remove_from_group(contact, group)
    contacts_in_group = db.get_contacts_in_group(group)
    contacts_not_in_group = db.get_contacts_not_in_group(group)
    assert contact in contacts_not_in_group
    assert contact not in contacts_in_group