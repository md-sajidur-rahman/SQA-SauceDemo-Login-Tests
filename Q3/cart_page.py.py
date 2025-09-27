from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def get_product_names(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]
    
    def get_item_count(self):
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items)
    
    def proceed_to_checkout(self):
        checkout_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()
        return self