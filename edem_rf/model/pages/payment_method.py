from selene.support.shared import browser
from selene import be


class PaymentMethod:

    def select_bank_card_method(self):
        browser.element('//div[contains(text(),"Банковской картой")]')\
            .should(be.visible).click()
        return self

    def submit_payment_method(self):
        browser.element('[type=submit]').click()
        return self