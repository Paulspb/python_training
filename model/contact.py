
class Contact:

    def __init__(self,firstname=None,lastName=None, midName=None, nickName=None, title=None, companyName=None, address1=None,
                 telHome=None, telMobile=None,telWork=None, fax=None,
                 email_1=None, email_2=None, email_3=None,
                 address_2=None, home_2=None, note_2=None, home_page=None, id=None):
        self.firstname  = firstname
        self.midName    = midName
        self.lastName   = lastName
        self.nickName   = nickName
        self.title      = title
        self.companyName = companyName
        self.address1    = address1
        self.telHome     = telHome
        self.telMobile   = telMobile
        self.telWork     = telWork
        self.fax         = fax
        self.email_1     = email_1
        self.email_2     = email_2
        self.email_3     = email_3
        self.address_2   = address_2
        self.home_2      = home_2
        self.note_2      = note_2
        self.home_page   = home_page
        self.id          = id
