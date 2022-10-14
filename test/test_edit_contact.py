from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="Admin", password="secret")
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
    app.contact.edit_first(contact)
    app.session.logout()