from datetime import datetime
from .base_page import BasePage
from .locators import TodoLocators
from .exceptions import MyError
from time import sleep
from selenium.webdriver.common.keys import Keys

# if U need log - use:
def logs_writer(log_message):
    """
    get log-message, add datetime to it, and push to log-file
    """
    today = datetime.today()
    output_message = str(today.strftime("%Y-%m-%d %H:%M:%S | ")) + log_message
    with open('logs/log_1.txt', 'a') as f:
        f.write(output_message)


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

        # find text in table for new item, check it:
        value_in_id_column = self.browser.find_element(*TodoLocators.value_in_id_column).text.strip()
        if value_in_id_column != '1':
            raise MyError('id in ID column != "1"')
        value_in_todo_column = self.browser.find_element(*TodoLocators.value_in_todo_column).text
        if value_in_todo_column != message:
            raise MyError(f'name must be {message}, title in item column = {value_in_todo_column}')
        value_in_priority_column = self.browser.find_element(*TodoLocators.value_in_priority_column).text.strip()
        if value_in_priority_column != 'important':
            log_message = 'case: EditTodo | priority in "Priority" column did not change'
            logs_writer(log_message)
            raise MyError(f'case: priority must be "important", priority in todo column = {value_in_priority_column}')


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


class SortById(BasePage):
    def sort_by_id(self, amount_of_items):
        """
        create list of items push it to the table, sort by ID few times, check for right sorting
        """
        list_of_items_names_and_priority = []
        for i in range(1, amount_of_items + 1):
            if i % 2 == 0:
                priority = 'secondary'
            else:
                priority = 'meh'
            list_of_items_names_and_priority.append([i, priority])

        # precomposition (make new items):
        for i in list_of_items_names_and_priority:
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
        list_of_items_in_id_column = self.browser.find_elements(*TodoLocators.list_of_items_by_id)
        list_of_text_of_items_in_id_column = []
        for i in list_of_items_in_id_column:
            list_of_text_of_items_in_id_column.append(i.text)
        list_for_compare_by_id_ascending = [str(x) for x in range(1, amount_of_items + 1)]  # create two compare-lists
        list_for_compare_by_id_descending = list_for_compare_by_id_ascending[::-1]
        if list_of_items_in_id_column != list_for_compare_by_id_ascending:
            raise MyError(f'list of items in ID column must be {list_for_compare_by_id_ascending}, '
                          f'have: {list_of_text_of_items_in_id_column} (ascending)')
        sort_by_id_btn.click()
        if list_of_items_in_id_column != list_for_compare_by_id_descending:
            raise MyError(f'list of items in ID column must be {list_for_compare_by_id_descending}, '
                          f'have: {list_of_text_of_items_in_id_column} (ascending')


class SortByTodo(BasePage):
    def sort_by_todo(self, amount_of_items):
        """
        create list of items push it to the table, sort by t0do column few times, check for right sorting
        """
        list_of_items_names_and_priority = []
        for i in range(1, amount_of_items + 1):
            if i % 2 == 0:
                priority = 'secondary'
            elif i % 3 == 0:
                priority = 'meh'
            else:
                priority = 'important'
            list_of_items_names_and_priority.append([i, priority])

        # precomposition (make new items):
        for i in list_of_items_names_and_priority:
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

        # checking for sorting by t0do column:
        sort_by_todo_btn = self.browser.find_element(*TodoLocators.sort_by_todo_btn)
        test_list_of_id_ascending = [str(x) for x in range(1, amount_of_items + 1)]  # create two lists of indexes
        test_list_of_id_descending = test_list_of_id_ascending[::-1]

        sort_by_todo_btn.click()

        list_of_items_in_todo_column = self.browser.find_elements(*TodoLocators.list_of_items_by_todo)
        list_of_text_of_items_in_todo_column = []
        for i in list_of_items_in_todo_column:
            list_of_text_of_items_in_todo_column.append(i.text)
        if list_of_text_of_items_in_todo_column != test_list_of_id_ascending:
            raise MyError(f'table has not sorting by Todo column (ascending)')

        sort_by_todo_btn.click()
        list_of_items_in_todo_column = self.browser.find_elements(*TodoLocators.list_of_items_by_todo)
        list_of_text_of_items_in_todo_column = []
        for i in list_of_items_in_todo_column:
            list_of_text_of_items_in_todo_column.append(i.text)
        if list_of_text_of_items_in_todo_column != test_list_of_id_descending:
            raise MyError(f'table has not sorting by Todo column (descending)')


class SortByPriority(BasePage):
    def sort_by_priority(self, amount_of_items):
        """
        create list of items push it to the table, sort by t0do column few times, check for right sorting
        """
        list_of_items_names_and_priority = []
        for i in range(1, amount_of_items + 1):
            if i % 2 == 0:
                priority = 'secondary'
            elif i % 3 == 0:
                priority = 'meh'
            else:
                priority = 'important'
            list_of_items_names_and_priority.append([i, priority])

        # excuse me for this part (create list for compare sorted by priority ascending):
        compare_list_ascending = []
        for i in list_of_items_names_and_priority:
            if i[1] == 'important':
                compare_list_ascending.append(i[1])
        for i in list_of_items_names_and_priority:
            if i[1] == 'meh':
                compare_list_ascending.append(i[1])
        for i in list_of_items_names_and_priority:
            if i[1] == 'secondary':
                compare_list_ascending.append(i[1])
        compare_list_descending = compare_list_ascending[::-1]  # reverse-list for compare descending sort

        # precomposition (make new items):
        for i in list_of_items_names_and_priority:
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

        # checking for sorted by priority:
        sort_by_priority_btn = self.browser.find_element(*TodoLocators.sort_by_priority_btn)
        sort_by_priority_btn.click()
        list_of_items_by_priority = self.browser.find_elements(*TodoLocators.list_of_items_by_priority)
        list_of_texts_in_items_sorted_by_priority = [item.text for item in list_of_items_by_priority]
        # first compare with descending, because list sorted by priority ascending as default
        if list_of_texts_in_items_sorted_by_priority != compare_list_descending:
            raise MyError(f'must be {compare_list_descending} have: {list_of_texts_in_items_sorted_by_priority} '
                          f'table has not sorting by priority column (descending)')
        sort_by_priority_btn.click()
        list_of_items_by_priority = self.browser.find_elements(*TodoLocators.list_of_items_by_priority)
        list_of_texts_in_items_sorted_by_priority = [item.text for item in list_of_items_by_priority]
        if list_of_texts_in_items_sorted_by_priority != compare_list_ascending:
            raise MyError(
                f'must be {compare_list_ascending} have: {list_of_texts_in_items_sorted_by_priority} '
                f'table has not sorting by priority column (ascending)')
