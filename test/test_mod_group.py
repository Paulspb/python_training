from model.group import Group

def test_mod_group(app):
    app.session.login( username="admin", password="secret")
    app.group.modify_first_group(Group(name="group1mod", header="group1Hmod", footer="group1Fmod"))
    app.session.logout()

