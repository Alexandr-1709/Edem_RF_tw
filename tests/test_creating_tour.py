import pickle
import time
from selene.support.shared import browser
import allure
from edem_rf.model import app
from allure_commons.types import Severity


@allure.tag("WEB UI")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Nikiforov")
@allure.title('Создание поездки')
def test_creating_tour():
    # GIVEN
    with allure.step('Открыть главную страницу'):
        app.main_page.open_page()
    with allure.step('Загрузка cookies'):
        app.main_page.load_cookies_in_profile()
    with allure.step('Открыть бургер-меню'):
        app.main_page.open_burger_menu()
    with allure.step('Проверка авторизации пользователя'):
        app.main_page.check_authorization()

    # WHEN
    with allure.step('Переход на страницу создания поездки'):
        app.main_page.open_create_tour_page()
    with allure.step('Поездка на авто'):
        app.car_tour_page.open_create_car_tour_page()
    with allure.step('Заполнение формы'):
        app.car_tour_page.fill_form()
    with allure.step('Переход далее с ознакомительной страницы'):
        app.smart_locator.next_page()
    with allure.step('Отказываемся от добавления промежуточных точек'):
        app.points_page.select_not_add_points()
    with allure.step('Заполнение даты и времени поездки'):
        app.date_time_tour.fill_date_time_tour_form()
    with allure.step('Подтверждение даты и времени'):
        app.date_time_tour.submit_date_time()

    with allure.step('Подтверждение автомобиля'):
        app.my_car.submit_my_car()

    with allure.step('Коментарий и Подтверждение деталей поездки'):
        app.details_tour.create_comments()
        app.details_tour.submit_detail()
    with allure.step('Установить цену за поездку и подтвердить'):
        app.price_tour.set_price()
        app.price_tour.submit_price()
    with allure.step('Выбрать cпособ оплаты он-лайн и подтвердить'):
        app.payment_method.select_bank_card_method()
        app.payment_method.submit_payment_method()
    with allure.step('Подтвердить карту-опубликовать поездку'):
        app.my_cart.to_publish()

    # THEN
    with allure.step('Проверка сообщения об успешной публикации'):
        app.my_ad.check_successful_publication()
    with allure.step('Проверка наличия поездки в листе поездок'):
        app.main_page.open_burger_menu()
        app.main_page.open_my_list_tour_page()
        app.list_tour.check_creation_tour()








# def test_auth_jwt_token():
# session = requests.Session()
# link = 'https://xn--d1abb2a.xn--p1ai/auth/login'
# headers = {
#     'Authorization': f'Bearer {jwt_token}'
# }
# persponce = session.post(link, headers=headers)
# response_profile = requests.get(profile_url, headers=headers).text
# print(response_profile)
