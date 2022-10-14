
def test_delete_first_group(app):
    app.session.login(username="Admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()