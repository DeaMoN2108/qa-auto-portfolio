import allure
from playwright.sync_api import Page
from ui_project.pages.base_page import BasePage
from ui_project.pages.components.header import HeaderComponent

class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header = HeaderComponent(page)

    @allure.step("Добавление товара '{item_name}' в корзину")
    def add_item_name(self, item_name: str):
        button = self.page.locator(f'[data-test="add-to-cart-{item_name}"]')
        button.click()