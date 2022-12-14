import re
from model.contact import Contact

def test_contact_on_home_page(app, db):
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
    contacts_from_home_page = app.contact.get_contacts_list()
    contacts_from_db = db.get_contacts_list()
    for contact in contacts_from_db:
        contact.emails_from_home_page = merge_like_on_home_page("emails", contact)
        contact.phones_from_home_page = merge_like_on_home_page("phones", contact)
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)

def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homenumber == contact_from_edit_page.homenumber
    assert contact_from_view_page.mobilenumber == contact_from_edit_page.mobilenumber
    assert contact_from_view_page.worknumber == contact_from_edit_page.worknumber
    assert contact_from_view_page.faxnumber == contact_from_edit_page.faxnumber
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(string):
    #remove '(', ')', ' ' and  '-'
    return re.sub("[() -]", "", string)

def merge_like_on_home_page(fields, contact):
    if fields == "phones":
        list = [contact.homenumber, contact.mobilenumber, contact.worknumber, contact.phone2]
        list = map(lambda x: clear(x), list)
    elif fields == "emails":
        list = [contact.email, contact.email2, contact.email3]
    else:
        raise ValueError(f"Unrecognized value for 'fields' parameter = {fields}")

    return "\n".join(
        filter(lambda x: x != "" and x is not None, list))

