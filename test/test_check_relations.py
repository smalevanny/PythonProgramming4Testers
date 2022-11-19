import random
from model.contact import Contact
from model.group import Group

def test_add_contact_to_group(app, orm):
    #we should have at least one contact
    if len(orm.get_contacts_list()) == 0:
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
    # we should have at least one group
    if len(orm.get_groups_list()) == 0:
        app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    groups = orm.get_groups_list()
    group = random.choice(groups)
    # we should have at least one contact, which is not in the group
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.remove_from_group(random.choice(orm.get_contacts_list()), group)
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts_not_in_group)
    print(contact)
    app.contact.add_to_group(contact, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    assert contact in contacts_in_group
    assert contact not in contacts_not_in_group

def test_delete_contact_from_group(app, orm):
    # we should have at least one contact
    if len(orm.get_contacts_list()) == 0:
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
    # we should have at least one group
    if len(orm.get_groups_list()) == 0:
        app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    contacts = orm.get_contacts_list()
    groups = orm.get_groups_list()
    group = random.choice(groups)
    # we should have at least one contact, which is in the group
    if len(orm.get_contacts_in_group(group)) == 0:
        app.contact.add_to_group(random.choice(contacts), group)
    contact = random.choice(orm.get_contacts_in_group(group))
    app.contact.remove_from_group(contact, group)
    contacts_in_group = orm.get_contacts_in_group(group)
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    assert contact in contacts_not_in_group
    assert contact not in contacts_in_group