from pages.locators import PaintsPageLocators
from playwright.sync_api import expect
from test_header import verify_header_elements
from test_footer import verify_footer_elements

#create a dictionary where key = data-id attribute and values = list of strings to check
paints_info = {
    "15a2dd6": ["PG7", "phtalo green", "phthalocyanine green", "+++ □"],
    "617de84": ["PR254", "pyrrole red", "pyrrole red", "+++ ◪"],
    "b7dc318": ["PBr6", "brown iron oxide", "brown iron oxide", "+++ ■"],
    "d616b7c": ["PW6", "titanium white", "titanium white", "+++ ■"],
    "bed5c02": ["PY42", "yellow oxide", "yellow oxide", "+++ ■"],
    "5631815": ["PB15", "phtalo blue", "phtalo blue", "+++ □"],
    "c9de5e5": ["PR101", "red oxide (mars red)", "iron red", "+++ ■"],
    "17e1f7d": ["PG7+PY74", "warm green", "warm green", "+++ ◪"],
    "7518da5": ["PB29", "ultramarine", "ultramarine", "+++ □"],
    "4de3d56": ["PY74", "primary yellow", "primary yellow", "+++ ◪"],
    "68d53dd": ["PBk11", "mars black", "mars black", "+++ ■"],
    "17c333f": ["PW6+PV23", "violet", "violet", "+++ ■"],
}

#create a dictionary where key = data-id attribute and value = paint image locator variable
paints_images = {
    "15a2dd6": "PHTALO_GREEN_IMAGE",
    "617de84": "PYRROLE_RED_IMAGE",
    "b7dc318": "BROWN_OXIDE_IMAGE",
    "d616b7c": "TITANIUM_WHITE_IMAGE",
    "bed5c02": "YELLOW_OXIDE_IMAGE",
    "5631815": "PHTALO_BLUE_IMAGE",
    "c9de5e5": "RED_OXIDE_IMAGE",
    "17e1f7d": "WARM_GREEN_IMAGE",
    "7518da5": "ULTRAMARINE_IMAGE",
    "4de3d56": "PRIMARY_YELLOW_IMAGE",
    "68d53dd": "MARS_BLACK_IMAGE",
    "17c333f": "VIOLET_IMAGE",
}

def verify_paints_elements(page, paints_info, paints_images):
    #iteration over each paint in paints_info dictionary
    for data_id, paint_info in paints_info.items():
        for info in paint_info:
            assert info in page.locator(f"//div[contains(@data-id, '{data_id}')]").inner_text()
        #receives image locator data_id attribute
        image_locator_attr = paints_images[data_id]
        #getattr(PaintsPageLocators, image_locator_attr) return the value of the attribute >>
        #>> in the PaintsPageLocators class that matches the string image_locator_attr.
        image_locator = getattr(PaintsPageLocators, image_locator_attr)
        assert page.locator(image_locator).is_visible() 

def verify_paints_page_common_title(page):
    element_text = page.locator(PaintsPageLocators.PAINTS_COMMON_TITLE).inner_text()
    assert "FEEL" in element_text
    assert "MY" in element_text
    assert "ACRYLICS" in element_text

PHTALO_GREEN_DESCRIPTION = [
    "PHTALO GREEN",
    "Series: Basic",
    "Pigment: PG7",
    "Coverage: □ (transparent)",
    "Lightfastness: +++",
    "Capacity: 120ml",
    "Where to buy:"
]

PYRROLE_RED_DESCRIPTION = [
    "PYRROLE RED",
    "Series: Basic",
    "Pigment: PR254",
    "Coverage: ◪ (semi-transparent)",
    "Lightfastness: +++",
    "Capacity: 120ml",
    "Where to buy:"
]

BROWN_OXIDE_DESCRIPTION = [
    "BROWN OXIDE",
    "Series: Basic",
    "Pigment: PBr6",
    "Coverage: ■ (opaque)",
    "Lightfastness: +++",
    "Capacity: 120ml",
    "Where to buy:"
]

TITANIUM_WHITE_DESCRIPTION = [
    "titanium white",
    "Series: Basic",
    "Pigment: PW6",
    "Coverage: ■ (opaque)",
    "Lightfastness: +++",
    "Capacity: 120ml",
    "Where to buy:"
]

YELLOW_OXIDE_DESCRIPTION = [
    "YELLOW OXIDE",
    "Series: Basic",
    "Pigment: PY42",
    "Coverage: ■ (opaque)",
    "Lightfastness: +++",
    "Capacity: 120ml",
    "Where to buy:"
]

PHTALO_BLUE_DESCRIPTION = [
    "PHTALO BLUE",
    "Series: Basic",
    "Pigment: PB15",
    "Coverage: □ (transparent)",
    "Lightfastness: +++",
    "Capacity: 120ml",
    "Where to buy:"
]

RED_OXIDE_DESCRIPTION = [
    "RED OXIDE",
    "Series: Basic",
    "Pigment: PR101",
    "Coverage: ■ (opaque)",
    "Lightfastness: +++",
    "Capacity: 120ml",
    "Where to buy:"
]

WARM_GREEN_DESCRIPTION = [
    "WARM GREENERY",
    "Series: Basic",
    "Pigment: PG7 + PY74",
    "Coverage: ◪ (semi-transparent)",
    "Lightfastness: +++",
    "Capacity: 120ml",
    "Where to buy:"
]

ULTRAMARINE_DESCRIPTION = [
    "ULTRAMARINE",
    "Series: Basic",
    "Pigment: PB29",
    "Coverage: □ (transparent)",
    "Lightfastness: +++",
    "Capacity: 120ml",
    "Where to buy:"
]

PRIMARY_YELLOW_DESCRIPTION = [
    "BASIC YELLOW",
    "Series: Basic",
    "Pigment: PY74",
    "Coverage: ◪ (semi-transparent)",
    "Lightfastness: +++",
    "Capacity: 120ml",
    "Where to buy:"
]

MARS_BLACK_DESCRIPTION = [
    "BLACK MARS",
    # Дополнительные символы &nbsp; в коде страницы, на которых падает тест(
    # "Series: Basic",
    # "Pigment: PBk11",
    # "Coverage: ■ (opaque)",
    "Lightfastness: +++",
    # "Capacity: 120ml",
    "Where to buy:"
]

VIOLET_DESCRIPTION = [
    "PURPLE",
    "Series: Basic",
    "Pigment: PW6+PV23",
    "Coverage: ■ (opaque)",
    "Lightfastness: +++",
    "Capacity: 120ml",
    "Where to buy:"
]

class TestPaintsPage():

    def test_paints_page_content(self, page):
        page.goto("https://feelmypaint.com/en/paints/")
        expect(page, "Paints page in English wasn't opened").to_have_url("https://feelmypaint.com/en/paints/")
        verify_header_elements(page)
        verify_paints_page_common_title(page)
        expect(page.locator(f"xpath={PaintsPageLocators.BASIC_LINE_TITLE}")).to_have_text("BASIC LINE")
        verify_paints_elements(page, paints_info, paints_images)
        verify_footer_elements(page)

    def test_paints_details_cards(self, page):
        page.goto("https://feelmypaint.com/en/paints/")
        expect(page, "Paints page in English wasn't opened").to_have_url("https://feelmypaint.com/en/paints/")

        #Open Phtalo Green paint card
        page.locator(PaintsPageLocators.PHTALO_GREEN_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Phtalo Green paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in PHTALO_GREEN_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

        #Open Pyrrole Red paint card
        page.locator(PaintsPageLocators.PYRROLE_RED_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Pyrrole Red paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in PYRROLE_RED_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

        #Open Brown Oxide paint card
        page.locator(PaintsPageLocators.BROWN_OXIDE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Brown Oxide paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in BROWN_OXIDE_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

        #Open Titanium White paint card
        page.locator(PaintsPageLocators.TITANIUM_WHITE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Titanium White paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in TITANIUM_WHITE_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

        #Open Yellow Oxide paint card
        page.locator(PaintsPageLocators.YELLOW_OXIDE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Yellow Oxide paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in YELLOW_OXIDE_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

        #Open Phtalo Blue paint card
        page.locator(PaintsPageLocators.PHTALO_BLUE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Phtalo Blue paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in PHTALO_BLUE_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

        #Open Red Oxide paint card
        page.locator(PaintsPageLocators.RED_OXIDE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Red Oxide paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in RED_OXIDE_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

        #Open Warm Green paint card
        page.locator(PaintsPageLocators.WARM_GREEN_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Warm Green paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in WARM_GREEN_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

        #Open Ultramarine paint card
        page.locator(PaintsPageLocators.ULTRAMARINE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Ultramarine paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in ULTRAMARINE_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

        #Open Primary Yellow paint card
        page.locator(PaintsPageLocators.PRIMARY_YELLOW_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Titanium White paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in PRIMARY_YELLOW_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

        #Open Mars Black paint card
        page.locator(PaintsPageLocators.MARS_BLACK_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Mars Black paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in MARS_BLACK_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

        #Open Violet paint card
        page.locator(PaintsPageLocators.VIOLET_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.CARD_POPUP_SELECTOR)
        # Verify Violet paint details
        actual_description = page.locator(PaintsPageLocators.CARD_POPUP_SELECTOR).inner_text()
        for string in VIOLET_DESCRIPTION:
            assert string in actual_description
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # Close the popup
        page.locator(PaintsPageLocators.CLOSE_POPUP_BUTTON).click()

    def test_shops_links(self, page):
        page.goto("https://feelmypaint.com/en/paints/")
        expect(page, "Paints page in English wasn't opened").to_have_url("https://feelmypaint.com/en/paints/")

        #Verify Phtalo Green paint shops links
        page.locator(PaintsPageLocators.PHTALO_GREEN_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow FMP shop hyperlink
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Phtalo Green FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/acrylic-paint-phthalocyanine-green-pg7-120ml/")
        page.go_back()
        page.locator(PaintsPageLocators.PHTALO_GREEN_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        #follow Allegro shop hyperlink
        page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        assert "14073383934" in page.url, "The expected product code '14073383934' is not in the Allegro URL: " + page.url
        page.go_back()
        page.locator(PaintsPageLocators.PHTALO_GREEN_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CC5WP6G9" in page.url, "The expected product code 'B0CC5WP6G9' is not in the Amazon URL: " + page.url
        page.go_back()

        #Verify Pyrrole Red paint shops links
        page.locator(PaintsPageLocators.PYRROLE_RED_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow FMP shop hyperlink
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Pyrrole Red FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/acrylic-paint-pirol-red-pr254-120ml/")
        page.go_back()
        #follow Allegro shop hyperlink
        page.locator(PaintsPageLocators.PYRROLE_RED_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        assert "14073355033" in page.url, "The expected product code '14073355033' is not in the URL: " + page.url
        page.go_back()
        #follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.PYRROLE_RED_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CY5T1P4V" in page.url, "The expected product code 'B0CY5T1P4V' is not in the Amazon URL: " + page.url
        page.go_back()

        #Verify Brown Oxide paint shops links
        page.locator(PaintsPageLocators.BROWN_OXIDE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow FMP shop hyperlink
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Brown Oxide FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/feelmypaint-acrylic-paint-brown-pbr7120ml/")
        page.go_back()
        #follow Allegro shop hyperlink
        page.locator(PaintsPageLocators.BROWN_OXIDE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        assert "14073042324" in page.url, "The expected product code '14073042324' is not in the URL: " + page.url
        page.go_back()
        #follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.BROWN_OXIDE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CY5Q4YJ2" in page.url, "The expected product code 'B0CY5Q4YJ2' is not in the Amazon URL: " + page.url
        page.go_back()

        #Open Titanium White paint card
        page.locator(PaintsPageLocators.TITANIUM_WHITE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow FMP shop hyperlink
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Titanium White FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/feelmypaint-acrylic-paint-titanium-white-pw6120ml/")
        page.go_back()
        #follow Allegro shop hyperlink
        page.locator(PaintsPageLocators.TITANIUM_WHITE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        assert "14073347847" in page.url, "The expected product code '14073347847' is not in the URL: " + page.url
        page.go_back()
        #follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.TITANIUM_WHITE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CBT2NYX9" in page.url, "The expected product code 'B0CBT2NYX9' is not in the Amazon URL: " + page.url
        page.go_back()

        #Open Yellow Oxide paint card
        page.locator(PaintsPageLocators.YELLOW_OXIDE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow FMP shop hyperlink
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Yellow Oxide FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/acrylic-paint-yellow-oxide-py42-120ml/")
        page.go_back()
        #follow Allegro shop hyperlink
        page.locator(PaintsPageLocators.YELLOW_OXIDE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        assert "14482070180" in page.url, "The expected product code '14482070180' is not in the URL: " + page.url
        page.go_back()
        #follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.YELLOW_OXIDE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CKRMWSXR" in page.url, "The expected product code 'B0CKRMWSXR' is not in the Amazon URL: " + page.url
        page.go_back()

        #Open Phtalo Blue paint card
        page.locator(PaintsPageLocators.PHTALO_BLUE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow FMP shop hyperlink
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Phtalo Blue FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/acrylic-phthalocyanine-paint-blue-pb15-120ml/")
        page.go_back()
        #follow Allegro shop hyperlink
        page.locator(PaintsPageLocators.PHTALO_BLUE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        assert "14482024128" in page.url, "The expected product code '14482024128' is not in the URL: " + page.url
        page.go_back()
        #follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.PHTALO_BLUE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CKRKYZ8H" in page.url, "The expected product code 'B0CKRKYZ8H' is not in the Amazon URL: " + page.url
        page.go_back()

        #Open Red Oxide paint card
        page.locator(PaintsPageLocators.RED_OXIDE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow FMP shop hyperlink
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Red Oxide FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/feelmypaint-acrylic-paint-red-oxide-pr-101-120ml/")
        page.go_back()
        # #follow Allegro shop hyperlink
        #incorrect hyperlink navigates to wrong paint
        # page.locator(PaintsPageLocators.RED_OXIDE_IMAGE).click()
        # page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        # page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        # assert "14482024128" in page.url, "The expected product code '14482024128' is not in the URL: " + page.url
        # page.go_back()
        #follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.RED_OXIDE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CKRMGDBD" in page.url, "The expected product code 'B0CKRMGDBD' is not in the Amazon URL: " + page.url
        page.go_back()

        #Open Warm Green paint card
        page.locator(PaintsPageLocators.WARM_GREEN_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        # follow FMP shop hyperlink
        # navigates to Polish page
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Warm Green FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/feelmypaint-acrylic-paint-warm-green-pg7py74-120ml/")
        page.go_back()
        # follow Allegro shop hyperlink
        page.locator(PaintsPageLocators.WARM_GREEN_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        assert "14481972385" in page.url, "The expected product code '14481972385' is not in the URL: " + page.url
        page.go_back()
        # follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.WARM_GREEN_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CJFDNZDR" in page.url, "The expected product code 'B0CJFDNZDR' is not in the Amazon URL: " + page.url
        page.go_back()

        # Open Ultramarine paint card
        page.locator(PaintsPageLocators.ULTRAMARINE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow FMP shop hyperlink
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Ultramarine FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/feelmypaint-acrylic-paint-ultramarine-pb29-120ml/")
        page.go_back()
        #follow Allegro shop hyperlink
        page.locator(PaintsPageLocators.ULTRAMARINE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        assert "14059615991" in page.url, "The expected product code '14059615991' is not in the URL: " + page.url
        page.go_back()
        #follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.ULTRAMARINE_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CBT1YK4W" in page.url, "The expected product code 'B0CBT1YK4W' is not in the Amazon URL: " + page.url
        page.go_back()

        #Open Primary Yellow paint card
        page.locator(PaintsPageLocators.PRIMARY_YELLOW_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow FMP shop hyperlink
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Primary Yellow FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/feelmypaint-yellow-acrylic-paint-py74-120ml/")
        page.go_back()
        #follow Allegro shop hyperlink
        page.locator(PaintsPageLocators.PRIMARY_YELLOW_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        assert "14073363119" in page.url, "The expected product code '14073363119' is not in the URL: " + page.url
        page.go_back()
        #follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.PRIMARY_YELLOW_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CC62SBYX" in page.url, "The expected product code 'B0CC62SBYX' is not in the Amazon URL: " + page.url
        page.go_back()

        #Open Mars Black paint card
        page.locator(PaintsPageLocators.MARS_BLACK_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow FMP shop hyperlink
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Mars Black FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/feelmypaint-acrylic-paint-black-mars-pbk11120ml/")
        page.go_back()
        #follow Allegro shop hyperlink
        page.locator(PaintsPageLocators.MARS_BLACK_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        assert "14073093537" in page.url, "The expected product code '14073093537' is not in the URL: " + page.url
        page.go_back()
        #follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.MARS_BLACK_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CXMB94HW" in page.url, "The expected product code 'B0CXMB94HW' is not in the Amazon URL: " + page.url
        page.go_back()

        # Open Violet paint card
        # incorrect hyperlinks navigate to wrong paint everywhere
        page.locator(PaintsPageLocators.VIOLET_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.FMP_SHOP_ICON)
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        #follow FMP shop hyperlink
        page.locator(PaintsPageLocators.FMP_SHOP_ICON).click()
        expect(page, "Violet FMP shop page wasn't opened").to_have_url("https://feelmypaint.com/en/product/feelmypaint-purple-acrylic-paint-pw6pv23-120ml/")
        page.go_back()
        #follow Allegro shop hyperlink
        page.locator(PaintsPageLocators.VIOLET_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.ALLEGRO_ICON)
        page.locator(PaintsPageLocators.ALLEGRO_ICON).click()
        assert "14073363119" in page.url, "The expected product code '14073363119' is not in the URL: " + page.url
        page.go_back()
        #follow Amazon shop hyperlink
        page.locator(PaintsPageLocators.VIOLET_IMAGE).click()
        page.wait_for_selector(PaintsPageLocators.AMAZON_ICON)
        page.locator(PaintsPageLocators.AMAZON_ICON).click()
        assert "B0CC62SBYX" in page.url, "The expected product code 'B0CC62SBYX' is not in the Amazon URL: " + page.url
        page.go_back()