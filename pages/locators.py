class HeaderLocators():
    MAIN_LOGO = "//*[@data-id='2848f75' and not(contains(@style, 'visibility: hidden'))]//img[contains(@src, 'https://feelmypaint.com/wp-content/uploads/2023/11/logologo.png')]"
    PAINTS_TOP_MENU_BUTTON = "//*[contains(@id, 'menu-1-7edf42c')]//a[contains(@href, 'paints')]"
    ABOUT_TOP_MENU_BUTTON = "//*[contains(@id, 'menu-1-7edf42c')]//a[contains(@href, 'about')]"
    HOW_TOP_MENU_BUTTON = "//*[contains(@id, 'menu-1-7edf42c')]//a[contains(@href, 'how')]"
    SHOP_TOP_MENU_BUTTON = "//*[contains(@id, 'menu-1-7edf42c')]//a[contains(@href, 'shop')]"
    CONTACT_TOP_MENU_BUTTON = "//*[contains(@id, 'menu-1-7edf42c')]//a[contains(@href, 'contact')]"
    LANGUAGE_CHOOSER_DROPDOWN = "*//li[contains(@class, 'menu-item') and contains(@class, 'wpml-ls-slot-4') and contains(@class, 'wpml-ls-current-language')]"
    CART = "//*[@id='elementor-menu-cart__toggle_button']"