from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
