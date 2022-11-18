import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    list = db.get_contacts_not_in_group(Group(id="91"))
    for item in list:
        print(item)
    print(len(list))
finally:
    pass #db.destroy()