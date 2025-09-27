@echo off
chcp 65001 >nul
title SauceDemo Performance User Test
color 0A

echo ==================================================
echo       SauceDemo Performance User Test
echo ==================================================
echo.

echo [1/4] Checking Python...
python --version
if errorlevel 1 (
    echo Error: Python not found. Install Python 3.8+ first.
    pause
    exit /b 1
)

echo.
echo [2/4] Installing packages...
pip install -r requirements.txt

echo.
echo [3/4] Running performance user test...
pytest tests/test_performance_user.py -v --alluredir=allure-results

echo.
echo [4/4] Creating test report...
allure generate allure-results -o allure-report --clean

echo.
echo ==================================================
echo                TEST FINISHED
echo ==================================================
echo.
echo Report generated: allure-report\index.html
echo.
echo Steps tested:
echo 1. Login with performance_glitch_user
echo 2. Reset app state
echo 3. Filter products Z to A
echo 4. Add first product to cart
echo 5. Complete checkout and verify
echo 6. Reset app and logout
echo.
echo Press any key to open the report folder...
pause >nul

if exist allure-report (
    explorer allure-report
)

echo.
echo Test complete. Check the report for details.
pause