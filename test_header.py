from playwright.sync_api import expect
from pages.locators import HeaderLocators

def verify_header_elements(page):
    expect(page.locator(f"xpath={HeaderLocators.MAIN_LOGO}")).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.PAINTS_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.PAINTS_TOP_MENU_BUTTON}").nth(0)).to_have_text("paints")
    expect(page.locator(f"xpath={HeaderLocators.ABOUT_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.ABOUT_TOP_MENU_BUTTON}").nth(0)).to_have_text("about")
    expect(page.locator(f"xpath={HeaderLocators.HOW_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.HOW_TOP_MENU_BUTTON}").nth(0)).to_have_text("how")
    expect(page.locator(f"xpath={HeaderLocators.SHOP_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.SHOP_TOP_MENU_BUTTON}").nth(0)).to_have_text("shop")
    expect(page.locator(f"xpath={HeaderLocators.CONTACT_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.CONTACT_TOP_MENU_BUTTON}").nth(0)).to_have_text("contact")
    expect(page.locator(f"xpath={HeaderLocators.LANGUAGE_CHOOSER_DROPDOWN}").nth(0)).to_be_visible()
    expect(page.locator(f"xpath={HeaderLocators.LANGUAGE_CHOOSER_DROPDOWN}").nth(0)).to_have_text("English")
    expect(page.locator(f"xpath={HeaderLocators.PAINTS_TOP_MENU_BUTTON}").nth(0)).to_be_visible()
    expect(page.locator(HeaderLocators.CART)).to_be_visible()
    expect(page.locator(HeaderLocators.CART)).to_contain_text("0,00")

class TestHeader():
    
    def test_header_elements_verification(self, page):
        page.goto("https://feelmypaint.com/en/")
        expect(page, "Site page in English wasn't opened").to_have_url("https://feelmypaint.com/en/")
        verify_header_elements(page)

    def test_header_hyperlinks(self, page):
        page.goto("https://feelmypaint.com/en/")
        expect(page, "Main page in English wasn't opened").to_have_url("https://feelmypaint.com/en/")
        page.locator(f"xpath={HeaderLocators.PAINTS_TOP_MENU_BUTTON}").nth(0).click()
        expect(page, "Paints page in English wasn't opened").to_have_url("https://feelmypaint.com/en/paints/")
        page.locator(f"xpath={HeaderLocators.ABOUT_TOP_MENU_BUTTON}").nth(0).click()
        expect(page, "About page in English wasn't opened").to_have_url("https://feelmypaint.com/en/about/")
        page.locator(f"xpath={HeaderLocators.HOW_TOP_MENU_BUTTON}").nth(0).click()
        expect(page, "How page in English wasn't opened").to_have_url("https://feelmypaint.com/en/how/")
        page.locator(f"xpath={HeaderLocators.SHOP_TOP_MENU_BUTTON}").nth(0).click()
        expect(page, "Shop page in English wasn't opened").to_have_url("https://feelmypaint.com/en/shop-2/")
        page.locator(f"xpath={HeaderLocators.CONTACT_TOP_MENU_BUTTON}").nth(0).click()
        expect(page, "Contact page in English wasn't opened").to_have_url("https://feelmypaint.com/en/contact/")
        page.locator(f"xpath={HeaderLocators.MAIN_LOGO}").nth(0).click()
        expect(page, "Main page in English wasn't opened").to_have_url("https://feelmypaint.com/en/")