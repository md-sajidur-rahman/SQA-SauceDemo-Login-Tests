@echo off
echo ========================================
echo    SauceDemo Locked User Test
echo ========================================
echo.

echo Step 1: Installing dependencies...
pip install -r requirements.txt

echo.
echo Step 2: Running the test...
pytest tests/test_locked_user.py -v --alluredir=allure-results

echo.
echo Step 3: Generating Allure report...
allure generate allure-results -o allure-report --clean

echo.
echo ========================================
echo            TEST COMPLETED
echo ========================================
echo.
echo Report generated: allure-report\index.html
echo.
echo To view the report:
echo 1. Open allure-report folder
echo 2. Double-click index.html
echo.
pause