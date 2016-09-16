from model.group import Group

def test_mod_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="add1"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="group1mod", header="group1Hmod", footer="group1Fmod"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)


def test_mod_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="add1"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="group1mod"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_mod_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="add1"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="group1Hmod"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

