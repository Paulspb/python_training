from model.group import Group
#less 7.4 from random import randrange
import random

def test_delete_some_group(app, db, check_ui):
    if db.get_group_list() == 0:
            # less 7.4 app.group.count() == 0:
        app.group.create(Group(name="add1"))
            #less 7.4 old_groups = app.group.get_group_list()
    old_groups = db.get_group_list()
        #less 7.4
    group = random.choice(old_groups)
        #less 7.3index = randrange(len(old_groups))
            # lesson 4.5 app.group.delete_first_group()
        #less 7.3 app.group.delete_group_by_index(index)
    app.group.delete_group_by_id(group.id)
    #less 7.3 new_groups = app.group.get_group_list()
    new_groups = db.get_group_list()
        # less 7.3 assert len(old_groups) - 1 == len(new_groups)
    # delete first element
        # lesson 4.5old_groups[0:1] = []
        # less 7.3 old_groups[index:index+1] = []
    old_groups.remove(group)
    assert old_groups == new_groups
        #less 7.5
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

