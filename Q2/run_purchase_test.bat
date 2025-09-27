@echo off
title SauceDemo Purchase Test
color 0A

echo ===============================================
echo      SauceDemo Purchase Flow Test
echo ===============================================
echo.

echo [1/4] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.8+ first.
    pause
    exit /b 1
)

echo.
echo [2/4] Installing required packages...
pip install -r requirements.txt

echo.
echo [3/4] Running the purchase flow test...
pytest tests/test_purchase_flow.py -v --alluredir=allure-results

echo.
echo [4/4] Generating test report...
allure generate allure-results -o allure-report --clean

echo.
echo ===============================================
echo               TEST COMPLETED
echo ===============================================
echo.
echo Report location: allure-report\index.html
echo.
echo To view the report:
echo 1. Open the 'allure-report' folder
echo 2. Double-click 'index.html'
echo.
echo Press any key to open the report folder...
pause >nul

explorer allure-report

echo.
echo Thank you for running the test!
pause