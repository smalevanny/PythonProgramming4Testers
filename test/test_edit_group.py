from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    app.group.edit_first(Group(name="Changed Group Name", header="Changed Group Header", footer="Changed Group Footer"))

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    app.group.edit_first(Group(name="New Group Name"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    app.group.edit_first(Group(header="New Group Header"))