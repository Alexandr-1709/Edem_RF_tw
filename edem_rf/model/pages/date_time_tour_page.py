from selene.support.shared import browser
from selene import be, have
import allure
from edem_rf.model.data.data_for_tests import tour_month, \
                                              tour_year, \
                                              date_number, \
                                              hour_tour, \
                                              minutes_tour


class DateTimeTour:

    def fill_date_time_tour_form(self):
        with allure.step('Выбрать дату'):
            browser.element('.js-routes-drafts-created-date-input').should(be.visible)
            browser.element('.js-routes-drafts-created-date-input').click()

            browser.element('//*[@id="datepickers-container"]/div[1]/nav/div[2]'). \
                should(have.text(tour_month)) and browser. \
                element('//*[@id="datepickers-container"]/div[1]/nav/div[2]'). \
                should(have.text(tour_year))
            elements = browser.element('//*[@id="datepickers-container"]/div[1]')
            elements.element('[data-date="%s"]' % date_number).click()

        with allure.step('Выбрать время'):
            browser.element('[name="createdTime"]').click()
            browser.element('.clockpicker-span-hours').should(be.visible).click()
            browser.element('//div[contains(@class, "clockpicker-tick")  and text() ="%s"]' % hour_tour).click()

            browser.element('.clockpicker-span-minutes').click()
            browser.element('//div[contains(@class, "clockpicker-tick")  and text() ="%s"]' % minutes_tour).click()

        return self

    def submit_date_time(self):
        browser.element('[type="submit"]').click()
        return self

