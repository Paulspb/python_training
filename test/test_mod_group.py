from model.group import Group

def test_mod_group(app):
    app.group.modify_first_group(Group(name="group1mod", header="group1Hmod", footer="group1Fmod"))


def test_mod_group_name(app):
    app.group.modify_first_group(Group(name="group1mod"))


def test_mod_group_header(app):
    app.group.modify_first_group(Group(header="group1Hmod"))


