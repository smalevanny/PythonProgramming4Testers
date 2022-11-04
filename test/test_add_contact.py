import string
from model.contact import Contact
import random
import pytest


def random_string(prefix, max_length):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


def random_word(max_length=10):
    symbols = string.ascii_letters.lower()
    return "".join([random.choice(symbols) for i in range(random.randrange(max_length))])


def random_email():
    return random_word() + "@" + random_word() + "." + random.choice(["ru", "com"])


def random_web_page():
    return "www." + random_word() + "." + random.choice(["ru", "com"])


def random_phone():
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(10)])

testdata = [Contact(firstname=random_string("firstname", 10),
                      middlename=random_string("middlename", 10),
                      lastname=random_string("lastname", 10),
                      nickname=random_string("nickname", 10),
                      title=random_string("title", 10),
                      company=random_string("company", 10),
                      address=random_string("address", 20),
                      homenumber=random_phone(),
                      mobilenumber=random_phone(),
                      worknumber=random_phone(),
                      faxnumber=random_phone(),
                      email=random_email(),
                      email2=random_email(),
                      email3=random_email(),
                      homepage=random_web_page(),
                      bday=str(1+random.randrange(20)),
                      bmonth=random.choice(["January", "March", "July", "September"]),
                      byear=str(1950 + random.randrange(50)),
                      aday=str(1+random.randrange(20)),
                      amonth=random.choice(["January", "March", "July", "September"]),
                      ayear=str(1950 + random.randrange(50)),
                      address2=random_string("address", 20),
                      phone2=random_phone(),
                      notes=random_string("address", 30),)
    for i in range(2)]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
