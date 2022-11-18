from selenium.webdriver.common.by import By

from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.groups_cache = None

    def delete_first(self):
        self.delete_by_index(1)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group(index)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.groups_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.groups_cache = None

    def edit_first(self, group):
        self.edit_by_index(1, group)

    def edit_by_index(self, index, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group(index)
        # init group edit
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(group)
        # submit group update
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.groups_cache = None

    def edit(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(group.id)
        # init group edit
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(group)
        # submit group update
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.groups_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)
    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def select_first_group(self):
        self.select_group(1)

    def select_group(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, f"input[value='{id}']").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    groups_cache = None

    def get_groups_list(self):
        if self.groups_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.groups_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.groups_cache.append(Group(name=text, id=id))
        return list(self.groups_cache)

