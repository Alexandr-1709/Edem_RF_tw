from selene.support.shared import browser
from selene import be, command


class EditTour:

    def remove_tour(self):
        browser.element('.js-account-routes-remove-handler')\
            .perform(command.js.scroll_into_view).click()
        browser.element('[type=submit]').should(be.visible)
        browser.element('[type=submit]').click()
        return self
