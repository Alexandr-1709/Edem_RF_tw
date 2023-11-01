from selene.support.shared import browser
from selene import command

"""Для данного тестового примера не будем реализовывть добавление
промежуточных точек"""


class IntermediatePoints:
    def select_add_points(self):
        pass

    def select_not_add_points(self):
        browser.element("//span[contains(text(),'Нет, спасибо')]").\
            perform(command.js.scroll_into_view).click()
        return self

