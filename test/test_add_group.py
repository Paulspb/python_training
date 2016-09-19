# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_String(prefix,maxlen):
    symbol = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


#testdata = [Group(name="", header="", footer="")] + [
#      Group(name=random_String("name",10),header=random_String("header",20),footer=random_String("footer",15))
#    for i in range(5)
#      # this is 5 time for random  + one 'empty'
#]

testdata = [
      Group(name=random_String("name1",10),header=random_String("header1",20),footer=random_String("footer1",15))
      # these means: name  and ... looping by "" or random value
    for name   in ["", random_String("name", 10)]
    for header in ["", random_String("header", 20)]
    for footer in ["", random_String("footer", 20)]
      # this is 5 time for random  + one 'empty'
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata ])
def test_add_group(app,group):
    for group in testdata:
        # less 5.4 def test_add_group(app):
        old_groups = app.group.get_group_list()
            # lesson 5.4     group = Group(name="group1", header="group1H", footer="group1F")
        app.group.create(group)
        # les 4.4 new_groups = app.group.get_group_list()
        # assert len(old_groups) + 1 == len(new_groups) lesson 4.4
        # this is hesh - function , as run faster as before !!!
        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key =Group.id_or_max)
# lesson 5.4
#def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    group = Group(name="", header="", footer="")
#    app.group.create(group)
#    assert len(old_groups) + 1 == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups.append(group)
#    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups,key =Group.id_or_max)
