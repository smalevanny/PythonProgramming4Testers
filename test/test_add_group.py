from model.group import Group

def test_add_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
