import allure
import pytest
from pages.login_page import LoginPage
from config import LOCKED_USER, PASSWORD, EXPECTED_ERROR

@allure.title("Test Locked User Login")
@allure.description("Verify error message when logging in with locked_out_user")
def test_locked_user_login(driver):
    
    with allure.step("Open login page"):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        allure.attach(driver.get_screenshot_as_png(), name="login_page", attachment_type=allure.attachment_type.PNG)
    
    with allure.step(f"Login with locked user: {LOCKED_USER}"):
        login_page.login(LOCKED_USER, PASSWORD)
        allure.attach(driver.get_screenshot_as_png(), name="after_login_attempt", attachment_type=allure.attachment_type.PNG)
    
    with allure.step("Check error message"):
        actual_error = login_page.get_error_message()
        
        assert actual_error is not None, "Error message should be displayed"
        assert actual_error == EXPECTED_ERROR, f"Expected: {EXPECTED_ERROR}, Got: {actual_error}"
        
        allure.attach(f"Expected: {EXPECTED_ERROR}\nActual: {actual_error}", 
                     name="error_verification", attachment_type=allure.attachment_type.TEXT)
        
        print(f"✓ Error message verified: {actual_error}")