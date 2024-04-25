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
    "617de84": "PIROLLE_RED_IMAGE",
    "b7dc318": "BROWN_OXIDE_IMAGE",
    "d616b7c": "TITANIUM_WHITE_IMAGE",
    "bed5c02": "YELLOW_OXIDE_IMAGE",
    "5631815": "PHTALO_BLUE_IMAGE",
    "c9de5e5": "MARS_RED_IMAGE",
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


class TestPaintsPage():

    def test_paints_page_content(self, page):
        page.goto("https://feelmypaint.com/en/paints/")
        expect(page, "Paints page in English wasn't opened").to_have_url("https://feelmypaint.com/en/paints/")
        verify_header_elements(page)
        verify_paints_elements(page, paints_info, paints_images)
        verify_footer_elements(page)
