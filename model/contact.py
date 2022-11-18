from sys import maxsize


class Contact:
    def __init__(self,
                 firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 title=None,
                 company=None,
                 address=None,
                 homenumber=None,
                 mobilenumber=None,
                 worknumber=None,
                 faxnumber=None,
                 email=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 bday=None,
                 bmonth=None,
                 byear=None,
                 aday=None,
                 amonth=None,
                 ayear=None,
                 address2=None,
                 phone2=None,
                 notes=None,
                 emails_from_home_page=None,
                 phones_from_home_page=None,
                 id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homenumber = homenumber
        self.mobilenumber = mobilenumber
        self.worknumber = worknumber
        self.faxnumber = faxnumber
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.emails_from_home_page = emails_from_home_page
        self.phones_from_home_page = phones_from_home_page
        self.id = id

    def __repr__(self):
        return f"{self.id}:{self.firstname}:{self.lastname}:{self.emails_from_home_page}:{self.phones_from_home_page}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname \
               and (self.emails_from_home_page is None or other.emails_from_home_page is None or self.emails_from_home_page == other.emails_from_home_page) \
               and (self.phones_from_home_page is None or other.phones_from_home_page is None or self.phones_from_home_page == other.phones_from_home_page)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize