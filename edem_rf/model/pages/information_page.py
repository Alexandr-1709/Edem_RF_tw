from selene.support.shared import browser
from selene import command


class SmartLocator:

    def next_page(self):
        browser.element('.js-info-locator-next-button').\
            perform(command.js.scroll_into_view).click()
        return self