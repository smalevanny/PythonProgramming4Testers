import random
from model.group import Group

def test_delete_group(app, db, check_ui):
    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_groups_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)