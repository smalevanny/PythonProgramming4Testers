from pony.orm import *
from datetime import datetime
from model.contact import Contact
from model.group import Group


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        address = Optional(str, column="address")
        email = Optional(str, column="email")
        email2 = Optional(str, column="email2")
        email3 = Optional(str, column="email3")
        homenumber = Optional(str, column="home")
        mobilenumber = Optional(str, column="mobile")
        worknumber = Optional(str, column="work")
        phone2 = Optional(str, column="phone2")
        deprecated = Optional(datetime, column="deprecated")
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind("mysql", host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def destroy(self):
        self.db.disconnect()

    def convert_to_groups_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_to_contacts_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname, address=contact.address,
                           email=contact.email, email2=contact.email2, email3=contact.email3,
                           homenumber=contact.homenumber, mobilenumber=contact.mobilenumber, worknumber=contact.worknumber, phone2=contact.phone2)
        return list(map(convert, contacts))


    @db_session
    def get_groups_list(self):
        return self.convert_to_groups_model(list(select(g for g in ORMFixture.ORMGroup)))

    @db_session
    def get_contacts_list(self):
        return self.convert_to_contacts_model(list(select(c for c in ORMFixture.ORMContact if c.deprecated is None)))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_to_contacts_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_to_contacts_model(list(select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups)))
