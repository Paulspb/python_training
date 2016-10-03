# -*- coding: utf-8 -*-
from model.group import Group
    # less 6.5 import pytest
    #from data.add_group import testdata
    #from data.groups import constant as testdata

    #less 6.3 move def random_String(prefix,maxlen):  -> data.addGroup.py

    #-revoke -less 6.5 @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata ])
    #-revoke- less 6.5def test_add_group(app,group):
    # it could be error if data_gorup , but not data_groups
        # less 6.6 def test_add_group(app, data_groups):
def test_add_group(app, json_groups):
    group = json_groups
            # -revoke less 6.3for group in testdata:
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
