from random import randrange
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
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
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="firstname2",
                      middlename="middlename2",
                      lastname="lastname2",
                      nickname="nickname2",
                      title="title2",
                      company="company2",
                      address="address2",
                      homenumber="homenumber2",
                      mobilenumber="mobilenumber2",
                      worknumber="worknumber2",
                      faxnumber="faxnumber2",
                      email="email",
                      email2="email2",
                      email3="email3",
                      homepage="homepage2",
                      bday="1",
                      bmonth="January",
                      byear="1981",
                      aday="2",
                      amonth="January",
                      ayear="2000",
                      address2="address2",
                      phone2="phone2",
                      notes="notes2")
    contact.id = old_contacts[index].id
    app.contact.edit(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)