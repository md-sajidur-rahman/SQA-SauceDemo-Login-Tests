from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import FIRST_NAME, LAST_NAME, ZIP_CODE

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def fill_checkout_info(self, first_name=FIRST_NAME, last_name=LAST_NAME, zip_code=ZIP_CODE):
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()
        return self
    
    def get_product_names(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]
    
    def get_total_price(self):
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
    
    def finish_order(self):
        self.driver.find_element(By.ID, "finish").click()
        return self
    
    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))).text
    
    def back_to_products(self):
        self.driver.find_element(By.ID, "back-to-products").click()
        return self