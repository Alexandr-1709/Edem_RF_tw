from selene.support.shared import browser
from selene import be


class CustomDetailsTour:

    def create_comments(self):
        browser.element('[name=comment]').should(be.visible).click()
        browser.element('[name=comment]').type('Весёлая будет поездочка!!!')
        return self

    def submit_detail(self):
        browser.element('[type=submit]').click()
        return self