from model.group import Group

def test_mod_group(app):
    if app.group.countContact() == 0:
        app.group.create(Group(name="add1"))
    old_groups = app.group.get_group_list()
    group = Group(name="group1mod", header="group1Hmod", footer="group1Fmod")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_mod_group_name(app):
    if app.group.countContact() == 0:
        app.group.create(Group(name="add1"))
    old_groups = app.group.get_group_list()
    group =  Group(name="group1mod")
    #group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    #old_groups[0] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_mod_group_header(app):
    if app.group.countContact() == 0:
        app.group.create(Group(name="add1"))
    old_groups = app.group.get_group_list()
    group = Group(header="group1Hmod")
    #group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    #old_groups[0] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

