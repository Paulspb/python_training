from model.group import Group
from random import randrange
import random

def test_mod_group(app, db):
    if db.get_group_list() == 0:
        app.group.create(Group(name="add1"))
            #less 7.4old_groups = app.group.get_group_list()
    old_groups = db.get_group_list()
            #less 7.4 index = randrange(len(old_groups))
    group_random = random.choice(old_groups)
    group = Group(name="group1mod", header="group1Hmod", footer="group1Fmod")
            # less 7.4 group.id = old_groups[index].id
    group.id = group_random.id
            # less 7.4 app.group.modify_group_by_index(index,group)
    app.group.modify_group_by_id(group_random.id, group)
            #less 7.4 new_groups = app.group.get_group_list()
    new_groups = db.get_group_list()
            #home 20
    old_groups.remove(group_random)
    old_groups.append(group)
    #assert len(old_groups)  == len(new_groups)
        ###old_groups.choice(group_random.id) = group
        ##old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_mod_group_name(app,db):
    if app.group.count() == 0:
        app.group.create(Group(name="add1"))
    old_groups = app.group.get_group_list()
    # less 7.4 index = randrange(len(old_groups))
    group_random = random.choice(old_groups)
    group =  Group(name="group1mod")
    # less 7.4 group.id = old_groups[0].id
    group.id = group_random.id
    app.group.modify_group_by_id(group_random.id, group)
    # less 7.4 new_groups = app.group.get_group_list()
    new_groups = db.get_group_list()
    # home 20
    old_groups.remove(group_random)
    old_groups.append(group)
    # assert len(old_groups)  == len(new_groups)
    ###old_groups.choice(group_random.id) = group
    ##old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_mod_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="add1"))
    old_groups = app.group.get_group_list()
    group = Group(header="group1Hmod")
    #group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    #old_groups[index] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

