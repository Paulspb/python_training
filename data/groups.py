from model.group import Group
#import random
#import string


# less 6.5
#constant = [
testdata = [
    Group(name="group1", header="group1H", footer="group1F"),
    Group(name="group2", header="group2H", footer="group2F")
]

# less 6.5
#def random_String(prefix,maxlen):
#    symbol = string.ascii_letters + string.digits + " "*10
#    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])#
#
#

#testdata = [Group(name="", header="", footer="")] + [
#      Group(name=random_String("name",10),header=random_String("header",20),footer=random_String("footer",15))
#    for i in range(5)
#      # this is 5 time for random  + one 'empty'
#]

#testdata = [
#      Group(name=random_String("name1",10),header=random_String("header1",20),footer=random_String("footer1",15))
#      # these means: name  and ... looping by "" or random value
#    for name   in ["", random_String("name", 10)]
#    for header in ["", random_String("header", 20)]
#    for footer in ["", random_String("footer", 20)]
#      # this is 5 time for random  + one 'empty'
#]

