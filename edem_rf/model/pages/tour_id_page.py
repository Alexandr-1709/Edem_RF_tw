from selene.support.shared import browser


class TourID:

    def open_pay_promo_tour(self):
        browser.element('.route-promo-package').click()
        return self

    def open_edit_tour_page(self):
        browser.element('.route-controls_paramount').click()
        return self

