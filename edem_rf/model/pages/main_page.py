import pickle
import time
from selene.support.shared import browser
from selene import be, have


def download_cookies_in_file():
    pickle.dump(browser.driver.get_cookies(), open('authorization_cookies', 'wb'))


class MainPage:

    def open_page(self):
        browser.open('')
        return self

    '''
       Загрузка cookies при ручной авторизации метод load_cookies
       pickle.dump(browser.driver.get_cookies(), open('authorization_cookies', 'wb'))
    '''

    def load_cookies_in_profile(self):
        for cookie in pickle.load(open('authorization_cookies', 'rb')):
            browser.driver.add_cookie(cookie)
        time.sleep(5.0)
        browser.driver.refresh()
        return self

    def open_burger_menu(self):
        browser.element('.header_button-menu').should(be.visible)
        browser.element('.header_button-menu').click()
        return self

    def check_authorization(self):
        browser.element('.header_menu-head_user-name').should(be.visible)
        browser.element('.header_menu-head_user-name').should(have.text('Анатолий'))
        return self

    def open_create_tour_page(self):
        browser.element('.header_menu-nav_link .link-tour_create').should(be.visible)
        browser.element('.header_menu-nav_link .link-tour_create').click()
        return self

    def open_my_list_tour_page(self):
        browser.element('//div[contains(text(), "Мои поездки")]').click()
        return self

    def open_wallet(self):
        browser.element('[href="/account/balance"].header_menu-nav_link').click()
        return self


