import allure
from playwright.sync_api import Page
from ui_project.pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.login_error_msg = page.locator('[data-test="error"]')
        self.login_container_error_msg = page.locator('[class="error-message-container error"]')
    @allure.step("Авторизация пользователя с логином {username} и паролем {password}")
    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()