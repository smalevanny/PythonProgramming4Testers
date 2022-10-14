from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="Admin", password="secret")
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
    app.session.logout()
