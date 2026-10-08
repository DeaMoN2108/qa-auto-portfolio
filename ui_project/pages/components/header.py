import allure, pytest
from playwright.sync_api import Page

class HeaderComponent:
    def __init__(self, page: Page):
        self.page = page
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    @allure.step("Переход в корзину через Header")
    def click_cart(self):
        self.cart_link.click()