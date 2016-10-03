from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


# from official doc
# n:      count of generated data
# n:      file name where it need to put
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of goups", "file ="])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f =  "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_String(prefix,maxlen):
    symbol = string.ascii_letters + string.digits + " " *10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="first2name", lastName="Last2name", midName="Mid2name", nickName="nick2name",
                    companyName="company12", address1="address112", telHome="homet2", telMobile="mobileT2",
                    telWork="wrokT2")] + [
            Contact(firstname=random_String("first_name",10), lastName=random_String("Last_name",20),
                               companyName=random_String("company1",20), address1=random_String("address11",20),
                                telHome=random_String("homet",20), telMobile=random_String("mobileT",10),telWork=random_String("wrokT",10),
                                email_1=random_String("email11",10), email_2=random_String("email2",10), email_3=random_String("email3",10),
                                home_2=random_String("home2",10))
            #for i in range (5)
            for i in range (n)
]


#-remove- less 6.5 file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contacts.json")
file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)

with open(file, "w") as out:
        #f.writable(json.dumps(testdata))
        # convert one line to several, where one line per attribute
    jsonpickle.set_encoder_options("json", indent=2)
    # -revoke- less 6.6 out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    out.write(jsonpickle.encode(testdata))