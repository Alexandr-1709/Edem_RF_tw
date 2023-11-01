from selene.support.shared import browser



class MyCar:

    def submit_my_car(self):
        browser.element('[type=submit]').click()
        return self
