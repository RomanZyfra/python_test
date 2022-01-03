from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="test1", header="test1", footer="test1"))

