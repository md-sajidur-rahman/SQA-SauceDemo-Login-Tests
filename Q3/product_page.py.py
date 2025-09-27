from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def get_cart_count(self):
        try:
            badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            return int(badge.text)
        except:
            return 0
    
    def sort_products_z_to_a(self):
        sort_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("za")
        return self
    
    def get_first_product_name(self):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        if products:
            return products[0].text
        return None
    
    def add_first_product_to_cart(self):
        add_buttons = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        if add_buttons:
            add_buttons[0].click()
            return True
        return False
    
    def go_to_cart(self):
        cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()
        return self
    
    def get_menu(self):
        from pages.menu_page import MenuPage
        return MenuPage(self.driver)