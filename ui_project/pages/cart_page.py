import allure
from ui_project.pages.base_page import BasePage
from ui_project.pages.components.header import HeaderComponent
from playwright.sync_api import Page

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.header = HeaderComponent(page)
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.inventory_item_name = page.locator('[data-test="inventory-item-name"]')
        self.continue_shopping_button = page.locator('[data-test="continue-shopping"]')
        self.remove_item_name_button = page.locator('[data-test="remove-sauce-labs-backpack"]')
        self.inventory_item_price = page.locator('[data-test="inventory-item-price"]')

    @allure.step("Получение списка названий товаров в корзине")
    def get_all_item_name(self):
        return self.inventory_item_name.all_inner_texts()
