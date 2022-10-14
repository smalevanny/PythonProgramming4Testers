import pytest
from application import Application
from group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="Admin", password="secret")
    app.create_group(Group(name="Group Name", header="Group Header", footer="Group Footer"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="Admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
