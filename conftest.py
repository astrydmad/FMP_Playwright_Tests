import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture(scope="session")
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        # all_cookies = context.cookies()
        # print(all_cookies)
        page.close()
        browser.close()

# @pytest.fixture(autouse=True)
# def cookies_fixture(browser_fixture: Page):
#     yield
#     all_cookies = browser_fixture.context.cookies()
#     print(all_cookies)

# @pytest.fixture
# def page(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     context.close()