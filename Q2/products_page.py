from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def get_cart_count(self):
        try:
            return int(self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text)
        except:
            return 0
    
    def add_three_products(self):
        # Find all add to cart buttons and click first three
        add_buttons = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        
        for i in range(min(3, len(add_buttons))):
            add_buttons[i].click()
        
        return self.get_cart_count()
    
    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return self
    
    def get_menu(self):
        from pages.menu_page import MenuPage
        return MenuPage(self.driver)
