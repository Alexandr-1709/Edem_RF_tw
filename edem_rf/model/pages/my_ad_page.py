from selene.support.shared import browser
from selene import have, be


class MyAd:

    def select_promotion_method(self):
        pass

    def to_pay(self):
        browser.element('[type=submit]').click()
        return self

    def check_successful_publication(self):
        browser.element('.create_route-success_caption').should(be.visible)
        browser.element('.create_route-success_caption').\
            should(have.text('опубликовано!'))
        return self
