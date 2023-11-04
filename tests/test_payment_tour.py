import time
import allure
from edem_rf.model import app
from allure_commons.types import Severity


@allure.tag("WEB UI")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Nikiforov")
@allure.title('Оплата поездки')
def test_payment_tour():
    # GIVEN
    with allure.step('Открыть главную страницу'):
        app.main_page.open_page()

    with allure.step('Загрузка cookies'):
        app.main_page.load_cookies_in_profile()

    # WHEN

    with allure.step('Открыть бургер-меню'):
        app.main_page.open_burger_menu()

    with allure.step('Открыть список поездок - "Мои поездки"'):
        app.main_page.open_my_list_tour_page()

    with allure.step('Открыть страницу с информацией о поездке'):
        app.list_tour.open_tour()

    with allure.step('Открыть страницу с информацией о поездке'):
        app.list_tour.open_tour()

    time.sleep(10)
        
        




