from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import FIRST_NAME, LAST_NAME, ZIP_CODE

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def fill_shipping_info(self):
        first_name_field = self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        first_name_field.send_keys(FIRST_NAME)
        
        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(LAST_NAME)
        
        zip_field = self.driver.find_element(By.ID, "postal-code")
        zip_field.send_keys(ZIP_CODE)
        
        continue_btn = self.driver.find_element(By.ID, "continue")
        continue_btn.click()
        
        return self
    
    def get_product_names(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]
    
    def get_total_price(self):
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total_element.text
    
    def complete_purchase(self):
        finish_btn = self.driver.find_element(By.ID, "finish")
        finish_btn.click()
        return self
    
    def get_success_message(self):
        success_element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        return success_element.text
    
    def back_to_products(self):
        back_btn = self.driver.find_element(By.ID, "back-to-products")
        back_btn.click()
        return self
