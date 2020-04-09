from .base_page import BasePage
from .locators import TodoLocators
from .exceptions import MyError
from time import sleep


class AddNewTodoWithOptions(BasePage):
    def add_new_important_todo(self, options):
        """
        options - list with
                [0] name of item that must be create
                [1] priority status of item that must be create
        """
        add_a_todo_btn = self.browser.find_element(*TodoLocators.add_a_todo_btn)
        add_a_todo_btn.click()
        new_todo_title_input = self.browser.find_element(*TodoLocators.new_todo_title_input)
        new_todo_title_input.send_keys(options[0])  # name
        if options[1] == 'important':
            new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_important_select)
            new_todo_priority_select.click()
        elif options[1] == 'secondary':
            new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_secondary_select)
            new_todo_priority_select.click()
        elif options[1] == 'meh':
            new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_meh_select)
            new_todo_priority_select.click()
        elif options[1] == '':  # case for empty priority value in select
            pass
        # sleep(1.5)  # if U want to see values in inputs
        new_todo_save_btn = self.browser.find_element(*TodoLocators.new_todo_save_btn)
        new_todo_save_btn.click()

        # find text in table for new item, check it
        value_in_id_column = self.browser.find_element(*TodoLocators.value_in_id_column).text.strip()
        if value_in_id_column != '1':
            raise MyError('id in ID column != 1')
        value_in_todo_column = self.browser.find_element(*TodoLocators.value_in_todo_column).text
        if value_in_todo_column != options[0]:
            raise MyError(f'name = {options[0]}, title in item column = {value_in_todo_column}')
        value_in_priority_column = self.browser.find_element(*TodoLocators.value_in_priority_column).text.strip()
        if value_in_priority_column != options[1]:
            raise MyError(f'priority = {options[1]}, priority in todo column = {value_in_priority_column}')




