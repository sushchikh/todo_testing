import pytest
from .pages.cases import AddNewTodoWithOptions, EditTodo, DeleteOneTodo, \
    DeleteAllTodos, SortById, SortByTodo, SortByPriority


url = 'http://91.217.196.36:5000'


# testing of create new item in items list
@pytest.mark.parametrize('options', [
    ['make important todo','important'],
    ['make secondary todo','secondary'],
    ['make meh todo','meh'],
    ['make None priority todo', '']])  # params - list of names and priority for new items
def test_add_new_important_todo(browser, options):
    page = AddNewTodoWithOptions(browser, url)
    page.open()
    page.add_new_important_todo(options)


# testing of edit item in list
@pytest.mark.parametrize('options', [
    ['do testing', 'meh']])
def test_edit_todo(browser, options):
    page = EditTodo(browser, url)
    page.open()
    page.edit_todo(options)


# testing of delete one item
@pytest.mark.parametrize('options', [
    ['do testing', 'meh']])  # param - name and priority of t0do
def test_delete_one_todo(browser, options):
    page = DeleteOneTodo(browser, url)
    page.open()
    page.delete_one_todo(options)


# testing delete all items
def test_delete_all_dodos(browser):
    page = DeleteAllTodos(browser, url)
    page.open()
    page.delete_all_todos()


# testing for sort by id
@pytest.mark.parametrize('amount_of_items', [9])  # param - amount of items
def test_sort_by_id(browser, amount_of_items):
    page = SortById(browser, url)
    page.open()
    page.sort_by_id(amount_of_items)


# testing for sort by t0do
@pytest.mark.parametrize('amount_of_items', [19])  # param - amount of items
def test_sort_by_todo(browser, amount_of_items):
    page = SortByTodo(browser, url)
    page.open()
    page.sort_by_todo(amount_of_items)


# testing for sort by priority
@pytest.mark.parametrize('amount_of_items', [19])  # param - amount of items
def test_sort_by_priority(browser, amount_of_items):
    page = SortByPriority(browser, url)
    page.open()
    page.sort_by_priority(amount_of_items)