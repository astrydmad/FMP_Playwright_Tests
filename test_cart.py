from playwright.sync_api import expect
from test_header import verify_header_elements
from pages.locators import HeaderLocators, Cart, ShopPageLocators, Cookies

def verify_cart_is_empty(page):
    expect(page.locator(HeaderLocators.CART)).to_be_visible()
    expect(page.locator(HeaderLocators.CART)).to_contain_text("0,00")
    page.locator(HeaderLocators.CART).nth(0).click()
    expect(page.locator(Cart.CART_PANEL)).to_be_visible()
    expect(page.locator(Cart.EMPTY_CART)).to_have_text("No products in the cart.")   

def verify_one_item_is_added_to_cart(page):
    expect(page.locator(HeaderLocators.CART)).to_be_visible()
    #проходит только если включен --headed
    page.wait_for_timeout(10000)
    expect(page.locator(HeaderLocators.CART)).to_contain_text("15,00 zł")
    expect(page.locator(Cart.QUANTITY_IN_CART)).to_contain_text("1")
    page.locator(HeaderLocators.CART).click()
    page.wait_for_timeout(3000)
    #count the number of items in cart
    number_of_items = page.locator(Cart.ADDED_ITEMS).locator(Cart.ADDED_ITEMS_LIST)
    assert number_of_items.count() == 1
    # number_of_delete_buttons = page.locator(Cart.REMOVE_ITEM_BUTTON)
    # assert number_of_delete_buttons.count == 1
    expect(page.locator(Cart.SUBTOTAL_SUM)).to_contain_text("15,00 zł")
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
        browser_fixture.locator(Cookies.ACCEPT_COOKIES).click()
        browser_fixture.locator(Cookies.SAVE_COOKIES_PREFERENCIES).click()
        browser_fixture.wait_for_timeout(3000)
        browser_fixture.locator(ShopPageLocators.RECENTLY_ADDED_SECOND_ITEM).click()
        expect(browser_fixture.locator(ShopPageLocators.VIEW_CART_RECENTLY_ADDED_SECOND_ITEM)).to_be_visible()
        verify_one_item_is_added_to_cart(browser_fixture)
        close_cart_panel(browser_fixture)
        


#     def test_add_product_from_paints_shop_page(self, page):

#     def test_add_product_from_sets_shop_page(self, page):

#     def test_add_main_product_from_product_page(self, page):

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