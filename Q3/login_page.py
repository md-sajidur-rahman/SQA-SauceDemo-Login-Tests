from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Longer wait for performance user
    
    def open_site(self):
        self.driver.get(BASE_URL)
        return self
    
    def login(self, username, password):
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_field.send_keys(username)
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        
        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()
        
        return self
    
    def is_login_successful(self):
        return "inventory" in self.driver.current_url
