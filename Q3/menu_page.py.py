from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open_menu(self):
        menu_btn = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu_btn.click()
        return self
    
    def reset_app_state(self):
        self.open_menu()
        
        reset_link = self.wait.until(EC.element_to_be_clickable((By.ID, "reset_sidebar_link")))
        reset_link.click()
        
        # Wait for reset to complete
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "bm-menu-wrap")))
        return self
    
    def logout(self):
        self.open_menu()
        
        logout_link = self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()
        
        return self