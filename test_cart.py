from playwright.sync_api import expect
from pages.locators import HeaderLocators, Cart, ShopPageLocators, Cookies, SinglePaintListShopPageLocators, SinglePaintPageLocators, SetsListShopPageLocators

def accept_all_cookies(page):
    page.locator(Cookies.ACCEPT_COOKIES).click()
    page.locator(Cookies.SAVE_COOKIES_PREFERENCIES).click()

def verify_cart_is_empty(page):
    expect(page.locator(HeaderLocators.CART)).to_be_visible()
    expect(page.locator(HeaderLocators.CART)).to_contain_text("0,00")
    page.locator(HeaderLocators.CART).nth(0).click()
    expect(page.locator(Cart.CART_PANEL)).to_be_visible()
    expect(page.locator(Cart.EMPTY_CART)).to_have_text("No products in the cart.")   

def verify_one_item_is_added_to_cart(page, expected_price):
    expect(page.locator(HeaderLocators.CART)).to_be_visible()
    #проходит только если включен --headed
    page.wait_for_timeout(10000)
    expect(page.locator(HeaderLocators.CART)).to_contain_text(expected_price)
    expect(page.locator(Cart.QUANTITY_IN_CART)).to_contain_text("1")
    page.locator(HeaderLocators.CART).click()
    page.wait_for_timeout(3000)
    #count the number of items in cart
    number_of_items = page.locator(Cart.ADDED_ITEMS).locator(Cart.ADDED_ITEMS_LIST)
    assert number_of_items.count() == 1
    # number_of_delete_buttons = page.locator(Cart.REMOVE_ITEM_BUTTON)
    # assert number_of_delete_buttons.count == 1
    expect(page.locator(Cart.SUBTOTAL_SUM)).to_contain_text(expected_price)
    expect(page.locator(Cart.VIEW_CART_BUTTON)).to_be_visible()
    expect(page.locator(Cart.CHECKOUT_BUTTON)).to_be_visible()

def close_cart_panel(page):
    page.locator(Cart.CHECKOUT_BUTTON).click()
    expect(page.locator(HeaderLocators.CART)).to_be_hidden()
    
class TestEmptyCart():

    def test_empty_cart(self, browser_fixture):
        browser_fixture.goto("https://feelmypaint.com/en/")
        expect(browser_fixture, "Main shop page in English wasn't opened").to_have_url("https://feelmypaint.com/en/")
        verify_cart_is_empty(browser_fixture)

class TestSingleAddToCart():

    def test_add_recently_added_product_from_main_shop_page(self, browser_fixture):
        browser_fixture.goto("https://feelmypaint.com/en/shop-2/")
        expect(browser_fixture, "Main shop page in English wasn't opened").to_have_url("https://feelmypaint.com/en/shop-2/")
        browser_fixture.wait_for_timeout(1000)
        accept_all_cookies(browser_fixture)
        browser_fixture.wait_for_timeout(1000)
        #get the item price
        price_before = browser_fixture.locator(ShopPageLocators.PRICE_RECENTLY_ADDED_SECOND_ITEM).inner_text()
        browser_fixture.locator(ShopPageLocators.RECENTLY_ADDED_SECOND_ITEM).click()
        expect(browser_fixture.locator(ShopPageLocators.VIEW_CART_RECENTLY_ADDED_SECOND_ITEM)).to_be_visible()
        verify_one_item_is_added_to_cart(browser_fixture, price_before)
        close_cart_panel(browser_fixture)

    def test_add_product_from_paints_shop_page(self, browser_fixture):
        browser_fixture.goto("https://feelmypaint.com/en/product-category/acrylic-paints/acrylic-paints-120ml-2/")
        expect(browser_fixture, "Main shop page in English wasn't opened").to_have_url("https://feelmypaint.com/en/product-category/acrylic-paints/acrylic-paints-120ml-2/")
        browser_fixture.wait_for_timeout(1000)
        accept_all_cookies(browser_fixture)
        browser_fixture.wait_for_timeout(1000)
        #get the item price
        price_before = browser_fixture.locator(SinglePaintListShopPageLocators.PRICE_ULTRAMARINE).inner_text()
        browser_fixture.locator(SinglePaintListShopPageLocators.ADD_TO_CART_BUTTON_ULTRAMARINE).click()
        expect(browser_fixture.locator(SinglePaintListShopPageLocators.VIEW_CART_ULTRAMARINE)).to_be_visible()
        verify_one_item_is_added_to_cart(browser_fixture, price_before)
        close_cart_panel(browser_fixture)

    def test_add_product_from_sets_shop_page(self, browser_fixture):
        browser_fixture.goto("https://feelmypaint.com/en/product-category/acrylic-paints/acrylic-paint-sets/")
        expect(browser_fixture, "Single paints shop page in English wasn't opened").to_have_url("https://feelmypaint.com/en/product-category/acrylic-paints/acrylic-paint-sets/")
        browser_fixture.wait_for_timeout(1000)
        accept_all_cookies(browser_fixture)
        browser_fixture.wait_for_timeout(1000)
        #get the item price
        price_before = browser_fixture.locator(SetsListShopPageLocators.PRICE_12_SET).inner_text()
        browser_fixture.locator(SetsListShopPageLocators.ADD_TO_CART_12_SET).click()
        expect(browser_fixture.locator(SetsListShopPageLocators.VIEW_CART_12_SET)).to_be_visible()
        verify_one_item_is_added_to_cart(browser_fixture, price_before)
        close_cart_panel(browser_fixture)

    def test_add_single_product_from_product_page(self, browser_fixture):
        browser_fixture.goto("https://feelmypaint.com/en/product/feelmypaint-yellow-acrylic-paint-py74-120ml/")
        expect(browser_fixture, "Yellow PY74 page in English wasn't opened").to_have_url("https://feelmypaint.com/en/product/feelmypaint-yellow-acrylic-paint-py74-120ml/")
        browser_fixture.wait_for_timeout(1000)
        accept_all_cookies(browser_fixture)
        browser_fixture.wait_for_timeout(3000)
        #get product title
        product_title = browser_fixture.locator(SinglePaintPageLocators.PRODUCT_PAGE_TITLE).inner_text()
        expected_popup_text = f"“{product_title}” has been added to your cart."

        browser_fixture.locator(SinglePaintPageLocators.ADD_TO_CART_PRODUCT_PAGE).click()
        browser_fixture.wait_for_timeout(1000)

        #get toasted notification text
        actual_popup_text = browser_fixture.locator(SinglePaintPageLocators.TOASTED_NOTIFICATION_MESSAGE).evaluate("element => element.lastChild.textContent.trim()")
        
        assert actual_popup_text == expected_popup_text, f"Expected popup text to be '{expected_popup_text}', but got '{actual_popup_text}'"
        expect(browser_fixture.locator(SinglePaintPageLocators.VIEW_CART_TOASTED_NOTIFICATION_BUTTON)).to_be_visible()
        verify_one_item_is_added_to_cart(browser_fixture)
        close_cart_panel(browser_fixture)

#     def test_add_related_product_from_product_page(self, page):

#     def test_add_own_set(self, page):

# class TestMultipleAddToCart():

#     def test_add_multiple_products_from_paints_shop_page(self, page):
        
#     def test_add_multiple_products_from_multiple_pages(self, page):

# class TestSingleRemoveFromCart():

#     def test_remove_product_from_cart_no_products_remain(self, page):
        
#     def test_remove_product_from_cart_one_product_remains(self, page):

# class TestMultipleRemoveFromCart():

#     def test_remove_multiple_products_from_cart_no_products_remain(self, page):

#     def test_remove_multiple_products_from_cart_multiple_products_remain(self, page):   


# class TestAddDeleteFromCart():

#     def test_add_product_delete_same_product(self, page):

#     def test_add_two_products_delete_one_product(self, page):

#     def test_add_two_products_delete_two_products(self, page):

#     def test_add_product_delete_product_add_product(self, page):