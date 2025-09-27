# SQA SauceDemo.com Login Tests
Test Scenarios: 

Test 1: Locked User Login
User: locked_out_user,
Test: Verify error message when trying to login with locked account,
Expected: "Epic sadface: Sorry, this user has been locked out".

Test 2: Standard User Purchase Flow
User: standard_user

Steps:
Login successfully,
Reset app state from hamburger menu,
Add any 3 products to cart,
Go to checkout and verify product names & total price,
Complete purchase and verify success message,
Reset app state again,
Logout.

Test 3: Performance User Filter & Purchase
User: performance_glitch_user

Steps:
Login successfully,
Reset app state,
Filter products by name (Z to A),
Add first product to cart,
Complete checkout and verify details,
Verify order success,
Reset app state again,
Logout. 

Python Packages:
Selenium
Pytest
Allure-Pytest
WebDriver-Manager
