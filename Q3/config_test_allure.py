import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Chrome setup
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    
    # Comment out headless to see the browser during test
    # options.add_argument("--headless")
    
    # Initialize driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    # Longer implicit wait for performance user
    driver.implicitly_wait(15)
    
    yield driver
    
    # Cleanup
    if driver:
        driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        driver = item.funcargs.get('driver')
        if driver:
            try:
                # Attach screenshot for each step
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"test_step_{report.nodeid}",
                    attachment_type=allure.attachment_type.PNG
                )
            except:
                pass
