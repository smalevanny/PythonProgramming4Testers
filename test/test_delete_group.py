from random import randrange
from model.group import Group

def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    app.group.delete(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups