from pages.locators import ShopPageLocators
from playwright.sync_api import expect
from test_header import verify_header_elements
from test_footer import verify_footer_elements

#create a dictionary where key = class name attribute
shop_paints_info = {
    "post-1544": {
        "src": "https://feelmypaint.com/wp-content/uploads/2023/11/fmp_black",
        "title": "FeelMyPaint Acrylic Paint Black Mars PBk11,120ml",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "1544"
    },
    "post-1529": {
        "src": "https://feelmypaint.com/wp-content/uploads/2024/03/fmp_brown-1",
        "title": "FeelMyPaint Acrylic Paint Brown PBr6,120ml",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "1529"
    },
    "post-1518": {
        "src": "https://feelmypaint.com/wp-content/uploads/2023/11/fmp_red",
        "title": "FeelMyPaint Acrylic Paint Pirol Red PR254, 120ml",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "1518"
    },
    "post-1535": {
        "src": "https://feelmypaint.com/wp-content/uploads/2023/11/fmp_white-1",
        "title": "FeelMyPaint Acrylic Paint Titanium White PW6,120ml",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "1535"
    },
    "post-1541": {
        "src": "https://feelmypaint.com/wp-content/uploads/2023/11/ultramarine",
        "title": "FeelMyPaint Acrylic Paint Ultramarine PB29, 120ml",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "1541"
    },
    "post-1547": {
        "src": "https://feelmypaint.com/wp-content/uploads/2023/11/fmp_green-1",
        "title": "FeelMyPaint Acrylic Paint Warm Green PG7+PY74, 120ml",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "1547"
    },
    "post-1519": {
        "src": "https://feelmypaint.com/wp-content/uploads/2023/11/fmp_yellow_shadow",
        "title": "FeelMyPaint Acrylic Paint Yellow Oxide PY42, 120ml",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "1519"
    },
    "post-1539": {
        "src": "https://feelmypaint.com/wp-content/uploads/2023/11/fmp_yellow",
        "title": "FeelMyPaint Acrylic Paint Yellow PY74, 120ml",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "1539"
    },
    "post-1534": {
        "src": "https://feelmypaint.com/wp-content/uploads/2023/11/fmp_blue_shadow",
        "title": "FeelMyPaint Acrylic Phthalocyanine Blue PB15, 120ml",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "1534"
    },
    "post-1530": {
        "src": "https://feelmypaint.com/wp-content/uploads/2023/11/fmp_green",
        "title": "FeelMyPaint Phthalocyanine Green Acrylic Paint PG7 120ml",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "1530"
    },
    "post-2167": {
        "src": "https://feelmypaint.com/wp-content/uploads/2024/03/fmp_tube_jpeg_shadow_violet",
        "title": "FeelMyPaint Purple Acrylic Paint PW6+PV23, 120ml.",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "2167"
    },
    "post-1538": {
        "src": "https://feelmypaint.com/wp-content/uploads/2023/11/fmp_red_shadow",
        "title": "FeelMyPaint Red Oxide Acrylic Paint PR101, 120ml",
        "price": "15,00",
        "currency": "zł",
        "button_text": "Add To Cart",
        "data-product_id": "1538"
    }

}

def verify_shop_main_info(page):
    page.wait_for_selector(ShopPageLocators.DELIVERY_ICON)
    expect(page.locator(f"xpath={ShopPageLocators.DELIVERY_TITLE}")).to_have_text("Express shipping")
    expect(page.locator(f"xpath={ShopPageLocators.DELIVERY_INFO}")).to_have_text("Express shipping Plenty of delivery options, shipping even in 24h!")
    page.wait_for_selector(ShopPageLocators.COMPLAINTS_RETURNS_ICON)
    expect(page.locator(f"xpath={ShopPageLocators.COMPLAINTS_RETURNS_TITLE}")).to_have_text("Complaints and returns")
    expect(page.locator(f"xpath={ShopPageLocators.COMPLAINTS_RETURNS_INFO}")).to_have_text("Complaints and returns We consider and implement fast and free")
    page.wait_for_selector(ShopPageLocators.GUARANTEE_ICON)
    expect(page.locator(f"xpath={ShopPageLocators.GUARANTEE_TITLE}")).to_have_text("GUARANTEE")
    expect(page.locator(f"xpath={ShopPageLocators.GUARANTEE_INFO}")).to_have_text("We are a manufacturer. Buy direct!")

def verify_single_paints_shop_elements(page, shop_paints_info):
    
    for class_name, paint_details in shop_paints_info.items():
        card_locator = f"//li[contains(@class, '{class_name}')]"

        # Verify paint image
        assert page.locator(f"{card_locator}//img[contains(@src, '{paint_details['src']}')]").is_visible()

        # Verify paint title
        assert paint_details['title'] in page.locator(f"{card_locator}//h2").inner_text()

        # Verify paint price
        assert paint_details['price'] in page.locator(f"{card_locator}//*[@class='price']").inner_text()

        # Verify currency
        assert paint_details['currency'] in page.locator(f"{card_locator}//*[@class='price']").inner_text()

        # Verify Add To Cart button
        assert paint_details['button_text'] in page.locator(f"{card_locator}//*[contains(@data-product_id, '{paint_details['data-product_id']}')]").inner_text()

class TestShopPage():

    def test_shop_page_content(self, page):
        page.goto("https://feelmypaint.com/en/shop-2/")
        expect(page, "Main shop page in English wasn't opened").to_have_url("https://feelmypaint.com/en/shop-2/")
        verify_header_elements(page)
        page.wait_for_selector(ShopPageLocators.PROMO_BANNER)
        verify_shop_main_info(page)
        page.wait_for_selector(ShopPageLocators.SINGLE_PAINT_ITEM_IMAGE)
        expect(page.locator(f"xpath={ShopPageLocators.SINGLE_PAINT_ITEM_HEADER}")).to_contain_text("Acrylic Paints 120ml")
        page.wait_for_selector(ShopPageLocators.SETS_IMAGE)
        expect(page.locator(f"xpath={ShopPageLocators.SETS_HEADER}")).to_contain_text("Acrylic Paint Sets")
        expect(page.locator(f"xpath={ShopPageLocators.RECENTLY_ADDED_HEADER}")).to_contain_text("Recently added products")
        #count the number of tiles in Recently added section
        li_elements = page.locator('div[data-id="8de0115"] div div ul li')
        assert li_elements.count() == 4
        verify_footer_elements(page)

    def test_shop_paints_content(self, page):
        page.goto("https://feelmypaint.com/en/shop-2/")
        expect(page, "Main shop page in English wasn't opened").to_have_url("https://feelmypaint.com/en/shop-2/")
        page.locator(ShopPageLocators.SINGLE_PAINT_ITEM_IMAGE).click()
        expect(page, "Single paints shop page in English wasn't opened").to_have_url("https://feelmypaint.com/en/product-category/acrylic-paints/acrylic-paints-120ml-2/")
        verify_header_elements(page)
        expect(page.locator(f"xpath={ShopPageLocators.SINGLE_PAINTS_LIST_HEADER}")).to_contain_text("All products in the category")
        verify_single_paints_shop_elements(page, shop_paints_info)
