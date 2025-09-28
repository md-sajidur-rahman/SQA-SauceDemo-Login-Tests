import allure
import pytest
from pages.login_page import LoginPage
from config import USERNAME, PASSWORD, ORDER_SUCCESS_MSG

class TestPurchaseFlow:
    
    @allure.title("Complete Purchase Journey Test")
    @allure.description("Login, reset app, add items, checkout, verify order, reset, logout")
    def test_complete_purchase_journey(self, driver):
        
        # Step 1: Login
        with allure.step("1. Login with standard_user"):
            login_page = LoginPage(driver)
            login_page.open_site().login(USERNAME, PASSWORD)
            assert login_page.is_logged_in(), "Login failed"
            allure.attach(driver.get_screenshot_as_png(), name="after_login", attachment_type=allure.attachment_type.PNG)
            print("✓ Logged in successfully")
        
        # Step 2: Reset App State
        with allure.step("2. Reset App State from menu"):
            products_page = login_page.driver
            menu = products_page.get_menu()
            menu.reset_app_state()
            cart_count = products_page.get_cart_count()
            assert cart_count == 0, "Cart should be empty after reset"
            allure.attach(driver.get_screenshot_as_png(), name="after_reset", attachment_type=allure.attachment_type.PNG)
            print("✓ App state reset")
        
        # Step 3: Add items to cart
        with allure.step("3. Add three items to cart"):
            items_added = products_page.add_three_products()
            assert items_added == 3, f"Expected 3 items, got {items_added}"
            allure.attach(driver.get_screenshot_as_png(), name="items_added", attachment_type=allure.attachment_type.PNG)
            print(f"✓ Added {items_added} items to cart")
        
        # Step 4: Go to cart and verify
        with allure.step("4. Navigate to cart"):
            cart_page = products_page.go_to_cart()
            item_count = cart_page.get_item_count()
            assert item_count == 3, f"Expected 3 items in cart, got {item_count}"
            product_names = cart_page.get_product_names()
            allure.attach(f"Products in cart: {', '.join(product_names)}", name="cart_contents", attachment_type=allure.attachment_type.TEXT)
            print(f"✓ Cart contains {item_count} items: {', '.join(product_names)}")
        
        # Step 5: Checkout
        with allure.step("5. Proceed to checkout"):
            checkout_page = cart_page.checkout()
            allure.attach(driver.get_screenshot_as_png(), name="checkout_page", attachment_type=allure.attachment_type.PNG)
            print("✓ Checkout page opened")
        
        # Step 6: Fill checkout info
        with allure.step("6. Fill checkout information"):
            checkout_page.fill_checkout_info()
            allure.attach(driver.get_screenshot_as_png(), name="checkout_info", attachment_type=allure.attachment_type.PNG)
            print("✓ Checkout information filled")
        
        # Step 7: Verify products and total
        with allure.step("7. Verify products and total price"):
            overview_products = checkout_page.get_product_names()
            total_price = checkout_page.get_total_price()
            
            assert len(overview_products) == 3, "Should have 3 products in overview"
            assert "Total" in total_price, "Total price should be displayed"
            
            allure.attach(f"Products: {', '.join(overview_products)}\nTotal: {total_price}", 
                         name="order_summary", attachment_type=allure.attachment_type.TEXT)
            print(f"✓ Order summary: {len(overview_products)} products, {total_price}")
        
        # Step 8: Complete purchase
        with allure.step("8. Complete purchase"):
            checkout_page.finish_order()
            success_msg = checkout_page.get_success_message()
            
            assert success_msg == ORDER_SUCCESS_MSG, f"Expected '{ORDER_SUCCESS_MSG}', got '{success_msg}'"
            allure.attach(driver.get_screenshot_as_png(), name="order_complete", attachment_type=allure.attachment_type.PNG)
            print(f"✓ Purchase completed: {success_msg}")
        
        # Step 9: Back to products and reset
        with allure.step("9. Return to products and reset app"):
            checkout_page.back_to_products()
            menu = products_page.get_menu()
            menu.reset_app_state()
            final_cart_count = products_page.get_cart_count()
            assert final_cart_count == 0, "Cart should be empty after final reset"
            allure.attach(driver.get_screenshot_as_png(), name="final_reset", attachment_type=allure.attachment_type.PNG)
            print("✓ App state reset again")
        
        # Step 10: Logout
        with allure.step("10. Logout from application"):
            menu.logout()
            assert "saucedemo" in driver.current_url and "inventory" not in driver.current_url
            allure.attach(driver.get_screenshot_as_png(), name="after_logout", attachment_type=allure.attachment_type.PNG)
            print("✓ Logged out successfully")
        
        print("\n🎉 All steps completed successfully!")
