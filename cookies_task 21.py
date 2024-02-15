from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Cookies:
    def __init__(self,url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def sleep(self,seconds):
        sleep(seconds)

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.sleep(5)

    def cookiesBeforeLogin(self):
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print(f"{cookie['name']}:{cookie['value']}")

    def inputBox(self, value, key):
        self.driver.find_element(by=By.NAME, value=value).send_keys(key)

    def submitBtn(self):
        self.driver.find_element(by=By.ID, value="login-button").click()
        self.sleep(10)

    def login(self):
        self.boot()
        self.inputBox("user-name", self.username)
        self.inputBox("password", self.password)
        self.submitBtn()

    def cookiesAfterLogin(self):
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print(f"{cookie['name']}:{cookie['value']}")

    def quit(self):
        self.driver.quit()


url = "https://www.saucedemo.com/"
obj = Cookies(url, "standard_user", "secret_sauce")
obj.login()
obj.cookiesBeforeLogin()
obj.cookiesAfterLogin()
obj.quit()

