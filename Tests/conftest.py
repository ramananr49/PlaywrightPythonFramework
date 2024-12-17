import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
@pytest.fixture
def invoke_Browser(playwright, request):
    browserName = request.config.getoption("browser_name")
    if browserName == "chrome":
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    elif browserName == "firefox":
        browser = playwright.firefox.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()
    browser.close()