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


