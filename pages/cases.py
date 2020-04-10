from .base_page import BasePage
from .locators import TodoLocators
from .exceptions import MyError
from time import sleep
from selenium.webdriver.common.keys import Keys

class AddNewTodoWithOptions(BasePage):
    """
    create items with different names and priority, check creation
    """
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
            raise MyError('id in ID column != "1"')
        value_in_todo_column = self.browser.find_element(*TodoLocators.value_in_todo_column).text
        if value_in_todo_column != options[0]:
            raise MyError(f'name must be {options[0]}, title in item column = {value_in_todo_column}')
        value_in_priority_column = self.browser.find_element(*TodoLocators.value_in_priority_column).text.strip()
        if value_in_priority_column != options[1]:
            raise MyError(f'priority must be {options[1]}, priority in todo column = {value_in_priority_column}')


class EditTodo(BasePage):
    def edit_todo(self, options):
        """
        create item change item name and priority, check changes
        """
        # precomposition (make new item):
        add_a_todo_btn = self.browser.find_element(*TodoLocators.add_a_todo_btn)
        add_a_todo_btn.click()
        new_todo_title_input = self.browser.find_element(*TodoLocators.new_todo_title_input)
        new_todo_title_input.send_keys(options[0])  # name
        new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_meh_select)
        new_todo_priority_select.click()
        new_todo_save_btn = self.browser.find_element(*TodoLocators.new_todo_save_btn)
        new_todo_save_btn.click()
        print('\ncreate "do testing" todo with "meh" priority')

        # edit element:
        edit_btn = self.browser.find_element(*TodoLocators.one_item_edit_btn)
        edit_btn.click()
        message = 'again ' + options[0]
        edit_todo_title_input = self.browser.find_element(*TodoLocators.edit_todo_title_input)

        edit_todo_title_input.send_keys(Keys.CONTROL + "a")
        edit_todo_title_input.send_keys(Keys.DELETE)
        edit_todo_title_input.send_keys(message)

        edit_todo_priority_important_select = self.browser.find_element(
            *TodoLocators.edit_todo_priority_important_select)
        edit_todo_priority_important_select.click()
        edit_todo_save_btn = self.browser.find_element(*TodoLocators.edit_todo_save_btn)
        edit_todo_save_btn.click()
        print('\nedit item, change name to "again testing" todo with "important" priority')

        # find text in table for new item, check it:
        value_in_id_column = self.browser.find_element(*TodoLocators.value_in_id_column).text.strip()
        if value_in_id_column != '1':
            raise MyError('id in ID column != "1"')
        value_in_todo_column = self.browser.find_element(*TodoLocators.value_in_todo_column).text
        if value_in_todo_column != message:
            raise MyError(f'name must be {message}, title in item column = {value_in_todo_column}')
        value_in_priority_column = self.browser.find_element(*TodoLocators.value_in_priority_column).text.strip()
        if value_in_priority_column != 'important':
            raise MyError(f'priority must be "important", priority in todo column = {value_in_priority_column}')


class DeleteOneTodo(BasePage):
    """
    create one item, delete it, check deleting
    """
    def delete_one_todo(self, options):
        # precomposition (make new item):
        add_a_todo_btn = self.browser.find_element(*TodoLocators.add_a_todo_btn)
        add_a_todo_btn.click()
        new_todo_title_input = self.browser.find_element(*TodoLocators.new_todo_title_input)
        new_todo_title_input.send_keys(options[0])  # name
        new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_meh_select)
        new_todo_priority_select.click()
        new_todo_save_btn = self.browser.find_element(*TodoLocators.new_todo_save_btn)
        new_todo_save_btn.click()
        print('\ncreate "do testing" todo with "meh" priority')

        # delete one item:
        delete_one_todo_popup_opener_btn = self.browser.find_element(*TodoLocators.delete_one_todo_popup_opener_btn)
        delete_one_todo_popup_opener_btn.click()
        delete_one_todo_submit_btn = self.browser.find_element(*TodoLocators.delete_one_todo_submit_btn)
        delete_one_todo_submit_btn.click()

        # is item deleted?
        items_table_tr = self.browser.find_element(*TodoLocators.items_table_tr)
        class_of_items_table_tr = items_table_tr.get_attribute("class")
        if class_of_items_table_tr != 'is-empty':
            raise MyError(f'table tr has not "is empty" value')
        print('\ncheck for emptiness table')


class DeleteAllTodos(BasePage):
    def delete_all_todos(self):
        """
        create list of items, push it to the table, delete all items
        """
        options_for_delete_all = []
        for i in range(1, 11):
            if i % 2 == 0:
                priority = 'secondary'
            else:
                priority = 'meh'
            options_for_delete_all.append([i, priority])

        # precomposition (make new items):
        for i in options_for_delete_all:
            add_a_todo_btn = self.browser.find_element(*TodoLocators.add_a_todo_btn)
            add_a_todo_btn.click()
            new_todo_title_input = self.browser.find_element(*TodoLocators.new_todo_title_input)
            new_todo_title_input.send_keys(i[0])  # name
            if i[1] == 'secondary':
                new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_secondary_select)
                new_todo_priority_select.click()
            if i[1] == 'meh':
                new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_meh_select)
                new_todo_priority_select.click()
            new_todo_save_btn = self.browser.find_element(*TodoLocators.new_todo_save_btn)
            new_todo_save_btn.click()
            sleep(1)
        print('\ncreate few items for mass-delete')

        # delete all items:
        delete_all_items_popup_opener_btn = self.browser.find_element(*TodoLocators.delete_all_items_popup_opener_btn)
        delete_all_items_popup_opener_btn.click()
        delete_all_items_submit_btn = self.browser.find_element(*TodoLocators.delete_all_items_submit_btn)
        delete_all_items_submit_btn.click()
        print('\ndelete all items')

        # is item deleted?
        items_table_tr = self.browser.find_element(*TodoLocators.items_table_tr)
        class_of_items_table_tr = items_table_tr.get_attribute("class")
        if class_of_items_table_tr != 'is-empty':
            raise MyError(f'table tr has not "is empty" value')
        else:
            print('\ntable is empty')

# TODO make right checking, now wrong list  
class SortById(BasePage):
    def sort_by_id(self):
        """
        create list of items push it to the table, sort by ID few times, check for right sorting
        """
        options_for_delete_all = []
        for i in range(1, 11):
            if i % 2 == 0:
                priority = 'secondary'
            else:
                priority = 'meh'
            options_for_delete_all.append([i, priority])

        # precomposition (make new items):
        for i in options_for_delete_all:
            add_a_todo_btn = self.browser.find_element(*TodoLocators.add_a_todo_btn)
            add_a_todo_btn.click()
            new_todo_title_input = self.browser.find_element(*TodoLocators.new_todo_title_input)
            new_todo_title_input.send_keys(i[0])  # name
            if i[1] == 'secondary':
                new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_secondary_select)
                new_todo_priority_select.click()
            if i[1] == 'meh':
                new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_meh_select)
                new_todo_priority_select.click()
            new_todo_save_btn = self.browser.find_element(*TodoLocators.new_todo_save_btn)
            new_todo_save_btn.click()
            sleep(1)
        print('\ncreate few items for mass-delete')

        # sorting by ID:

        sort_by_id_btn = self.browser.find_element(*TodoLocators.sort_by_id_btn)
        sort_by_id_btn.click()

        # if U want to see how wrong it work uncomment code below
        # sleep(2)
        # sort_by_id_btn.click()
        # sleep(2)
        # sort_by_id_btn.click()
        # sleep(2)
        # sort_by_id_btn.click()
        # sleep(2)

        # checking for sorting by ID (compare with two right lists of indexes)
        list_of_items_by_id = self.browser.find_elements(*TodoLocators.list_of_items_by_id)

        test_list_of_id_1 = [x for x in range(1, 11)] # create two lists of indexes
        test_list_of_id_2 = test_list_of_id_1[::-1]
        if list_of_items_by_id != test_list_of_id_1:
            raise MyError('table has not sorting by IDs (ascending)')
        else:
            print('\nsort by ID work well (ascending)')
        sort_by_id_btn.click()
        if list_of_items_by_id != test_list_of_id_2:
            raise MyError('table has not sorting by IDs (descending)')
        else:
            print('\nsort by ID work well (descending)')



class SortByTodo(BasePage):
    def sort_by_todo(self, options):
        """
        create list of items push it to the table, sort by t.do column few times, check for right sorting
        """
        options_for_delete_all = []
        for i in range(1, options+1):
            if i % 2 == 0:
                priority = 'secondary'
            elif i % 3 == 0:
                priority = 'meh'
            else:
                priority = 'important'
            options_for_delete_all.append([i, priority])

        # precomposition (make new items):
        for i in options_for_delete_all:
            add_a_todo_btn = self.browser.find_element(*TodoLocators.add_a_todo_btn)
            add_a_todo_btn.click()
            new_todo_title_input = self.browser.find_element(*TodoLocators.new_todo_title_input)
            new_todo_title_input.send_keys(i[0])  # name
            if i[1] == 'secondary':
                new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_secondary_select)
                new_todo_priority_select.click()
            if i[1] == 'meh':
                new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_meh_select)
                new_todo_priority_select.click()
            if i[1] == 'important':
                new_todo_priority_select = self.browser.find_element(*TodoLocators.new_todo_priority_important_select)
                new_todo_priority_select.click()
            new_todo_save_btn = self.browser.find_element(*TodoLocators.new_todo_save_btn)
            new_todo_save_btn.click()
        print('\ncreate few items for mass-delete')

        sleep(1)


        # checking for sorting by t0do column:
        unsorted_list_of_items_by_todo = self.browser.find_element(*TodoLocators.list_of_items_by_todo)
        sort_by_todo_btn = self.browser.find_element(*TodoLocators.sort_by_todo_btn)
        test_list_of_id_ascending = [str(x) for x in range(1, options+1)]  # create two lists of indexes
        test_list_of_id_descending = test_list_of_id_ascending[::-1]

        sort_by_todo_btn.click()

        list_of_items_in_todo_column = self.browser.find_elements(*TodoLocators.list_of_items_by_todo)
        list_of_text_of_items_in_todo_column = []
        for i in list_of_items_in_todo_column:
            list_of_text_of_items_in_todo_column.append(i.text)
        if list_of_text_of_items_in_todo_column != test_list_of_id_ascending:
            raise MyError(f'table has not sorting by Todo column (ascending)')
        else:
            print('\nsort by ID work well (ascending)')
        sort_by_todo_btn.click()
        sleep(3)
        list_of_items_in_todo_column = self.browser.find_elements(*TodoLocators.list_of_items_by_todo)
        list_of_text_of_items_in_todo_column = []
        for i in list_of_items_in_todo_column:
            list_of_text_of_items_in_todo_column.append(i.text)
        if list_of_text_of_items_in_todo_column != test_list_of_id_descending:
            raise MyError(f'table has not sorting by Todo column (descending)')
        else:
            print('\nsort by ID work well (descending)')

