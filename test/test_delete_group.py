from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    app.group.delete_first()