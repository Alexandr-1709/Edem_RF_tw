from selene.support.shared import browser



class MyCart:

    def create_cart(self):
        pass

    def to_publish(self):
        browser.element('[type=submit]').click()
        return self
