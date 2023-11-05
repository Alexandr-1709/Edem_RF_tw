import allure
from selene.support.shared import browser
from selene import be, command
from edem_rf.model.data.data_for_tests import city_from, city_to


class CarTourPage:
    def open_create_car_tour_page(self):
        browser.element('// div[contains(text(), "Поездка на автомобиле")]') \
            .should(be.visible)
        browser.element('// div[contains(text(), "Поездка на автомобиле")]') \
            .click()
        return self

    def fill_form(self):
        with allure.step('откуда - куда'):
            browser.element('#js-routes-drafts-select-search-from') \
                .should(be.visible)
            browser.element('#js-routes-drafts-select-search-from').click(). \
                type(city_from)

            elements = browser.element('.form-dropdown-city')
            elements.element("//div[contains(text(),'Екатеринбург')]").click()

            # element.click().all('option').element_by(have.value(your_value)).click()
            browser.element('[name = "fromAddress"]').click(). \
                type('м. Ботаническая')

            browser.element('#js-routes-drafts-select-search-to').click(). \
                type(city_to)

            elements = browser.element('.form-dropdown-city')
            elements.element("//div[contains(text(),'Пермь')]").click()

            browser.element('[name = "toAddress"]').click(). \
                type('Автовокзал')

        with allure.step('Переход далее'):
            browser.element('[type="submit"]') \
                .perform(command.js.scroll_into_view)
            browser.element('[type="submit"]') \
                .click()
        return self
