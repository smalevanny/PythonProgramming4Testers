from model.group import Group


# def test_edit_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(name="Changed Group Name", header="Changed Group Header", footer="Changed Group Footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    old_groups = app.group.get_group_list()
    group = Group(name="New Group Name")
    group.id = old_groups[0].id
    app.group.edit_first(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(header="New Group Header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)