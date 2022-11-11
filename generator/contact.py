import jsonpickle
import os.path
import random
import string
from model.contact import Contact
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))