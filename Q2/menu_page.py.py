from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open_menu(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        return self
    
    def reset_app_state(self):
        self.open_menu()
        self.wait.until(EC.element_to_be_clickable((By.ID, "reset_sidebar_link"))).click()
        # Wait for menu to close
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "bm-menu-wrap")))
        return self
    
    def logout(self):
        self.open_menu()
        self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
        return self