from selene.support.shared import browser
from selene import have

from edem_rf.model.data.data_for_tests import city_to, city_from


class ListTour:
    def open_tour(self):
        browser.element('.account-routes_list').click()
        return self

    def check_empty_list_tour(self):
        browser.element('.route-empty_content').should(have.text('У вас нет активных поездок и грузоперевозок'))
        return self

    def check_creation_tour(self):
        browser.element('.account-routes_list').should(have.text(city_from)) and \
        browser.element('.account-routes_list').should(have.text(city_to))
        return self
