import pickle
import time

from selene.support.shared import browser
import requests

import allure
from edem_rf.model import app
from allure_commons.types import Severity

from edem_rf.model.data.data_for_tests import jwt_token, base_url, user_url, profile_url


@allure.tag("WEB UI")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Nikiforov")
@allure.title('Создание поездки')
def test_creating_a_trip():
    # GIVEN
    with allure.step('Открыть главную страницу'):
        app.main_page.open_page()

    # with allure.step('Открыть бургер-меню'):
    #     app.main_page.open_burger_menu()
    # with allure.step('Проверка нахождения на странице авторизации'):
    #     app.login_page.check_transition_to_login_page()


def test_auth_jwt_token():
    # session = requests.Session()
    # link = 'https://xn--d1abb2a.xn--p1ai/auth/login'
    headers = {
        'Authorization': f'Bearer {jwt_token}'
    }
    # persponce = session.post(link, headers=headers)
    response_profile = requests.get(profile_url, headers=headers).text

    print(response_profile)

