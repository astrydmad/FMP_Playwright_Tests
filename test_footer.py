from playwright.sync_api import Playwright, sync_playwright, expect
from pages.locators import HeaderLocators


def test_footer_elements_verification(page):
    page.goto("https://feelmypaint.com/en/")
    expect(page, "Site page in English wasn't opened").to_have_url("https://feelmypaint.com/en/")
    # main_logo = page.query_selector(f"xpath={HeaderLocators.MAIN_LOGO}")
    expect(page.locator(f"xpath={HeaderLocators.MAIN_LOGO}")).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.PAINTS_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.ABOUT_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.HOW_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.SHOP_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.CONTACT_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.LANGUAGE_CHOOSER_DROPDOWN}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.PAINTS_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.CART}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.CART}").nth(0)).to_contain_text("0,00")

# def test_footer_hyperlinks(page):
    # page.get_by_role("link", name="farby").click()
    # page.get_by_role("link", name="o nas").click()
    # page.get_by_role("link", name="jak").click()
    # page.get_by_role("link", name="sklep", exact=True).click()
    # page.get_by_role("link", name="kontakt").click()