from selene.support.shared import browser
from selene import have


class MyAd:

    def select_promotion_method(self):
        pass

    def to_pay(self):
        browser.element('[type=submit]').click()
        return self

    def check_successful_publication(self):
        browser.element('[type=submit]').should(have.text('Объявление опубликовано!'))
