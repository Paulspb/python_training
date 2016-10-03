from model.group import Group
import random
import string
import os.path
    #less 6.6 -revoke-   import json
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
f =  "data/groups.json"
# script paramater could be fill-in   -n 6 if data\test_group.json

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_String(prefix,maxlen):
    symbol = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
      Group(name=random_String("name",10),header=random_String("header",20),footer=random_String("footer",15))
      # for i in range (5)
      for i in range(n)
      # this is 5 time for random  + one 'empty'
]

# define path file  ../ as file defined into -generator- dir
# #file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/group.json")
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

#define writubng to file  , where .dumps  convert structure to json-format
with open(file, "w") as out:
        #f.writable(json.dumps(testdata))
            # it need to clarify how to convert -Group- to json where __dict__ keeps all __init__
        #    f.write(json.dumps(testdata, default=lambda x: x.__dict__))
            # now split one line to several lines
    jsonpickle.set_encoder_options("json", indent=2)
        #-revoke- less 6.6 out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    out.write(jsonpickle.encode(testdata))