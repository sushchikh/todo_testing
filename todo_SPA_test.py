import pytest
from .pages.cases import AddNewTodoWithOptions, EditTodo, DeleteOneTodo, DeleteAllTodos, SortById


url = 'http://91.217.196.36:5000'


# testing of create new item in items list
@pytest.mark.parametrize('options', [
    ['make important todo','important'],
    ['make secondary todo','secondary'],
    ['make meh todo','meh'],
    ['make None priority todo', '']])
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
    ['do testing', 'meh']])
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
def test_sort_by_id(browser):
    page = SortById(browser, url)
    page.open()
    page.sort_by_id()
