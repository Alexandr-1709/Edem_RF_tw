from selene.support.shared import browser
from selene import be


class PriceTour:

    def set_price(self):
        browser.element('.js-routes-drafts-costs-input').should(be.visible).click()
        browser.element('.js-routes-drafts-costs-input').clear().type('500')
        return self

    def submit_price(self):
        browser.element('[type=submit]').click()
        return self
