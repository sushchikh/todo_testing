import pytest
from .pages.cases import AddNewTodoWithOptions


url = 'http://91.217.196.36:5000'


# parametrized test for create new item in items list
@pytest.mark.parametrize('options', [
    ['make important todo','important'],
    ['make secondary todo','secondary'],
    ['make meh todo','meh'],
    ['make None priority todo', '']])
def test_add_new_important_todo(browser, options):
    page = AddNewTodoWithOptions(browser, url)
    page.open()
    page.add_new_important_todo(options)


