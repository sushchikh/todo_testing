# create class with browser for test, set implicitly wait for elements
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # задаем время ожидания для браузера

    def open(self):
        self.browser.get(self.url)

