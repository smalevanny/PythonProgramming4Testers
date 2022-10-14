from model.group import Group


def test_edit_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.edit_first(Group(name="Changed Group Name", header="Changed Group Header", footer="Changed Group Footer"))
    app.session.logout()