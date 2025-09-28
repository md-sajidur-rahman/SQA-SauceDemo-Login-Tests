import allure
import pytest
from pages.login_page import LoginPage
from config import USERNAME, PASSWORD, SUCCESS_MESSAGE

class TestPerformanceUser:
    
    @allure.title("Performance User Purchase Journey")
    @allure.description("Login with performance_glitch_user, filter Z-A, add first product, complete purchase")
    def test_performance_user_purchase(self, driver):
        
        print("Starting performance user test...")
        
        # Step 1: Login
        with allure.step("1. Login with performance_glitch_user"):
            login_page = LoginPage(driver)
            login_page.open_site()
            login_page.login(USERNAME, PASSWORD)
            
            assert login_page.is_login_successful(), "Login failed for performance user"
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
        
        # Step 3: Filter products Z to A
        with allure.step("3. Filter products by name (Z to A)"):
            products_page.sort_products_z_to_a()
            first_product_name = products_page.get_first_product_name()
            
            assert first_product_name is not None, "Should have products after sorting"
            allure.attach(driver.get_screenshot_as_png(), name="after_sorting", attachment_type=allure.attachment_type.PNG)
            print(f"✓ Products sorted Z-A. First product: {first_product_name}")
        
        # Step 4: Add first product to cart
        with allure.step("4. Add first product to cart"):
            added = products_page.add_first_product_to_cart()
            assert added, "Should be able to add product to cart"
            
            cart_count = products_page.get_cart_count()
            assert cart_count == 1, "Cart should have 1 item"
            allure.attach(driver.get_screenshot_as_png(), name="product_added", attachment_type=allure.attachment_type.PNG)
            print(f"✓ Added product to cart. Cart count: {cart_count}")
        
        # Step 5: Go to cart and verify
        with allure.step("5. Navigate to cart"):
            cart_page = products_page.go_to_cart()
            item_count = cart_page.get_item_count()
            product_names = cart_page.get_product_names()
            
            assert item_count == 1, f"Should have 1 item in cart, got {item_count}"
            allure.attach(f"Product in cart: {product_names[0]}", name="cart_product", attachment_type=allure.attachment_type.TEXT)
            print(f"✓ Cart contains: {product_names[0]}")
        
        # Step 6: Checkout
        with allure.step("6. Proceed to checkout"):
            checkout_page = cart_page.proceed_to_checkout()
            allure.attach(driver.get_screenshot_as_png(), name="checkout_start", attachment_type=allure.attachment_type.PNG)
            print("✓ Checkout page opened")
        
        # Step 7: Fill shipping info
        with allure.step("7. Fill shipping information"):
            checkout_page.fill_shipping_info()
            allure.attach(driver.get_screenshot_as_png(), name="shipping_info", attachment_type=allure.attachment_type.PNG)
            print("✓ Shipping information filled")
        
        # Step 8: Verify product and total
        with allure.step("8. Verify product and total price"):
            overview_products = checkout_page.get_product_names()
            total_price = checkout_page.get_total_price()
            
            assert len(overview_products) == 1, "Should have 1 product in overview"
            assert "Total" in total_price, "Total price should be displayed"
            
            allure.attach(f"Product: {overview_products[0]}\nTotal: {total_price}", 
                         name="order_overview", attachment_type=allure.attachment_type.TEXT)
            print(f"✓ Order overview - Product: {overview_products[0]}, Total: {total_price}")
        
        # Step 9: Complete purchase
        with allure.step("9. Complete purchase"):
            checkout_page.complete_purchase()
            success_msg = checkout_page.get_success_message()
            
            assert success_msg == SUCCESS_MESSAGE, f"Expected '{SUCCESS_MESSAGE}', got '{success_msg}'"
            allure.attach(driver.get_screenshot_as_png(), name="order_complete", attachment_type=allure.attachment_type.PNG)
            print(f"✓ Purchase completed: {success_msg}")
        
        # Step 10: Back to products and reset
        with allure.step("10. Return to products and reset app"):
            checkout_page.back_to_products()
            menu = products_page.get_menu()
            menu.reset_app_state()
            
            final_cart_count = products_page.get_cart_count()
            assert final_cart_count == 0, "Cart should be empty after final reset"
            allure.attach(driver.get_screenshot_as_png(), name="final_reset", attachment_type=allure.attachment_type.PNG)
            print("✓ App state reset again")
        
        # Step 11: Logout
        with allure.step("11. Logout from application"):
            menu.logout()
            assert "saucedemo" in driver.current_url and "inventory" not in driver.current_url
            allure.attach(driver.get_screenshot_as_png(), name="after_logout", attachment_type=allure.attachment_type.PNG)
            print("✓ Logged out successfully")
        
        print("\n🎉 Performance user test completed successfully!")
