
from selene.support.shared import browser
from selene import be, have



class MainPage:

    def open_page(self):
        browser.open('')

        return self

    def open_burger_menu(self):
        browser.element('.header_button-menu').should(be.visible)
        browser.element('.header_button-menu').click()
        return self
