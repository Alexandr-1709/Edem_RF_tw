import time
import allure
from edem_rf.model import app
from allure_commons.types import Severity

from edem_rf.model.data.data_for_tests import standart_pay_posting


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

    with allure.step('Запомнить баланс до оплаты и перейти обратно в меню'):
        app.main_page.open_wallet()
        balance_before = app.wallet.get_balance()
        app.main_page.open_burger_menu()

    with allure.step('Открыть список поездок - "Мои поездки"'):
        app.main_page.open_my_list_tour_page()

    with allure.step('Открыть страницу с информацией о поездке'):
        app.list_tour.open_tour()

    with allure.step('Открыть страницу оплаты/продвижения объявления'):
        app.tour_id.open_pay_promo_tour()

    with allure.step('Выбрать способ оплаты "Стандарт"'):
        app.pay_posting.standart_pay_posting()

    with allure.step('Произвести и подтвердить оплату'):
        app.pay_posting.submit_pay_posting()
        app.pay_posting.confirm_pay()

    #THEN
    with allure.step('Проверить, что оплата прошла и средства списались'):
        app.pay_posting.check_success_pay_posting()

        app.main_page.open_burger_menu()
        app.main_page.open_wallet()
        balance_after = app.wallet.get_balance()
    assert balance_before - int(standart_pay_posting) == balance_after


        
        




