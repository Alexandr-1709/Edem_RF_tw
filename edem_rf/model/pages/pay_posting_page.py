from selene.support.shared import browser
from selene import be

from edem_rf.model.data.data_for_tests import standart_pay_posting


class PayPosting:

    def standart_pay_posting(self):
        browser.element('//div[contains(text(), "%s")]' % standart_pay_posting).should(be.visible)
        browser.element('//div[contains(text(), "%s")]' % standart_pay_posting).click()
        return self

    def standart_plus_pay_posting(self):
        pass

    def premium_pay_posting(self):
        pass

    def submit_pay_posting(self):
        browser.element('[type=submit]').click()
        return self

    def confirm_pay(self):
        browser.element('[method=post] [type=submit]').should(be.visible)
        browser.element('[method=post] [type=submit]').click()
        return self

    def check_success_pay_posting(self):
        browser.element('//h5[contains(text(), "Операция прошла успешно!")]') \
            .should(be.visible)
        browser.element('//h5[contains(text(), "Операция прошла успешно!")]') \
            .click()
        return self
