from playwright.sync_api import expect
from pages.locators import FooterLocators
from pages.locators import Cookies

def verify_footer_elements(page):
    expect(page.locator(f"xpath={FooterLocators.ACCOUNT}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.CHECKOUT}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.CART}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.SHOP}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.PRIVACY_POLISY}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.REGULATIONS}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.TRANSPORTATION_DELIVERY}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.PAYMENTS}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.COMPLAINTS_RETURNS}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.FOOTER_FMP_LOGO}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.COMPANY_INFO}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.COMPANY_EMAIL}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.COMPANY_NIP}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.YOUTUBE_ICON_FOOTER}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.INSTAGRAM_ICON_FOOTER}")).to_be_visible()
    expect(page.locator(f"xpath={FooterLocators.FACEBOOK_ICON_FOOTER}")).to_be_visible()
    
class TestFooter():

    def test_footer_elements_verification(self, page):
        page.goto("https://feelmypaint.com/en/")
        expect(page, "Site page in English wasn't opened").to_have_url("https://feelmypaint.com/en/")
        verify_footer_elements(page)


    def test_header_hyperlinks(self, page):
        page.goto("https://feelmypaint.com/en/")
        expect(page, "Main page in English wasn't opened").to_have_url("https://feelmypaint.com/en/")
        # expect(page.locator(f"xpath={Cookies.ACCEPT_COOKIES}")).to_be_visible()
        # # page.locator(f"xpath={Cookies.ACCEPT_COOKIES}").click()
        page.locator(f"xpath={FooterLocators.ACCOUNT}").click()
        expect(page, "Account page in English wasn't opened").to_have_url("https://feelmypaint.com/en/my-account-2/")
        page.locator(f"xpath={FooterLocators.CHECKOUT}").click()
        expect(page, "Cart page in English wasn't opened").to_have_url("https://feelmypaint.com/en/cart-2/")
        page.locator(f"xpath={FooterLocators.CART}").click()
        expect(page, "Cart page in English wasn't opened").to_have_url("https://feelmypaint.com/en/cart-2/")
        page.locator(f"xpath={FooterLocators.SHOP}").click()
        expect(page, "Shop page in English wasn't opened").to_have_url("https://feelmypaint.com/en/shop-2/")
        page.locator(f"xpath={FooterLocators.PRIVACY_POLISY}").click()
        expect(page, "Privacy Policy page in English wasn't opened").to_have_url("https://feelmypaint.com/en/privacy-policy/")
        page.locator(f"xpath={FooterLocators.REGULATIONS}").click()
        expect(page, "Store Regulations page in English wasn't opened").to_have_url("https://feelmypaint.com/en/store-regulations/")
        page.locator(f"xpath={FooterLocators.TRANSPORTATION_DELIVERY}").click()
        expect(page, "Delivery time and costs page in English wasn't opened").to_have_url("https://feelmypaint.com/en/transportation-costs-and-delivery-time/")
        page.locator(f"xpath={FooterLocators.PAYMENTS}").click()
        expect(page, "Payments page in English wasn't opened").to_have_url("https://feelmypaint.com/en/payment-methods/")
        page.locator(f"xpath={FooterLocators.COMPLAINTS_RETURNS}").click()
        expect(page, "Complaints and Returns page in English wasn't opened").to_have_url("https://feelmypaint.com/en/complaints-and-returns/")
        # page.locator(f"xpath={FooterLocators.YOUTUBE_ICON_FOOTER}").click()
        # expect(page, "Youtube page in English wasn't opened").to_have_url("https://www.youtube.com/@FeelMyPaint")
        # page.locator(f"xpath={FooterLocators.INSTAGRAM_ICON_FOOTER}").click()
        # expect(page, "Instagram page in English wasn't opened").to_have_url("https://www.instagram.com/feelmypaint_official/")
        # page.locator(f"xpath={FooterLocators.FACEBOOK_ICON_FOOTER}").click()
        # expect(page, "Facebook page in English wasn't opened").to_have_url("https://www.facebook.com/feelmypaintpl")