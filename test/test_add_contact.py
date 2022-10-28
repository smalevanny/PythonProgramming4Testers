from model.contact import Contact

def test_add_contact(app):
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
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
