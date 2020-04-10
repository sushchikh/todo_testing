# locators for elements on SPA
# excuse me for using XPATH selector, better way use ID, I know, but where they?
from selenium.webdriver.common.by import By


class TodoLocators():
    add_a_todo_btn = (By.CSS_SELECTOR, "#app > div > section > div > div.level > button.button.is-primary")
    new_todo_title_input = (By.CSS_SELECTOR, '#app > div > div > div.animation-content > div > section > div:nth-child(1) > div > input')
    new_todo_priority_important_select = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/section/div[2]/div/span/select/option[@value="important"]')
    new_todo_priority_secondary_select = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/section/div[2]/div/span/select/option[1]')
    new_todo_priority_meh_select = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/section/div[2]/div/span/select/option[3]')
    new_todo_save_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/footer/button[2]')

    value_in_id_column = (By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div[2]/table/tbody/tr/td[1]')
    value_in_todo_column = (By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div[2]/table/tbody/tr/td[2]')
    value_in_priority_column = (By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div[2]/table/tbody/tr/td[3]')

    one_item_edit_btn = (By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div[2]/table/tbody/tr/td[4]/button/span')
    edit_todo_title_input = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/section/div[1]/div/input')
    edit_todo_save_btn = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/footer/button[2]')
    edit_todo_priority_important_select = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/section/div[2]/div/span/select/option[2]')

    delete_one_todo_popup_opener_btn = (By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div[2]/table/tbody/tr/td[5]/button/span/i')
    delete_one_todo_submit_btn = (By.XPATH, '/html/body/div[2]/div[2]/footer/button[2]')
    items_table_tr = (By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div[2]/table/tbody/tr')

    delete_all_items_popup_opener_btn = (By.XPATH, '//*[@id="app"]/div/section/div/div[1]/button[2]/span')
    delete_all_items_submit_btn = (By.XPATH, '/html/body/div[2]/div[2]/footer/button[2]')

    list_of_items_by_id = (By.CSS_SELECTOR, '#app > div > section > div > div.b-table > div.table-wrapper > table > tbody > tr > td:nth-child(1)')
    sort_by_id_btn = (By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div[2]/table/thead/tr/th[1]/div')
    list_of_items_by_todo = (By.CSS_SELECTOR, '#app > div > section > div > div.b-table > div.table-wrapper > table > tbody > tr > td:nth-child(2)')
    sort_by_todo_btn = (By.XPATH, '//*[@id="app"]/div/section/div/div[2]/div[2]/table/thead/tr/th[2]/div')
