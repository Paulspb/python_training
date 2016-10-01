from model.contact import Contact
import random
import string


testdata = [
    Contact(firstname="first22name", lastName="Last22name", midName="Mid22name", nickName="nick22name",
            companyName="company22", address1="address1122", telHome="homet22", telMobile="mobileT22",
            telWork="wrokT22"),
    Contact(firstname="first232name", lastName="Last232name", midName="Mid232name", nickName="nick232name",
            companyName="company232", address1="address11232", telHome="homet232", telMobile="mobileT232",
            telWork="wrokT232")
]

#def random_String(prefix,maxlen):
#    symbol = string.ascii_letters + string.digits + " " *10
#    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


#testdata = [Contact(firstname="first2name", lastName="Last2name", midName="Mid2name", nickName="nick2name",
#                    companyName="company12", address1="address112", telHome="homet2", telMobile="mobileT2",
#                    telWork="wrokT2")] + [
#            Contact(firstname=random_String("first_name",10), lastName=random_String("Last_name",20),
#                               companyName=random_String("company1",20), address1=random_String("address11",20),
#                                telHome=random_String("homet",20), telMobile=random_String("mobileT",10),telWork=random_String("wrokT",10),
#                                email_1=random_String("email11",10), email_2=random_String("email2",10), email_3=random_String("email3",10),
#                                home_2=random_String("home2",10))
#            for i in range (6)
#]

