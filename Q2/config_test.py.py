import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Chrome options
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    # Remove headless for visibility during test
    # options.add_argument("--headless")
    
    # Setup driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    driver.implicitly_wait(10)
    
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
            # Always attach screenshot for each test
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"step_{report.nodeid}",
                    attachment_type=allure.attachment_type.PNG
                )
            except:
                pass