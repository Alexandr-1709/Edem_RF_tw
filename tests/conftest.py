import pytest
from selene.support.shared import browser
from edem_rf.model.data.data_for_tests import base_url, jwt_token, user_url, profile_url


@pytest.fixture(scope='function', autouse=True)
def driver_management_remote():
    browser.config.base_url = base_url
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 5.0

    yield browser
    browser.quit()

# @pytest.fixture()
# def load_cookies(driver_management_remote):
#     for cookie in pickle.load(open('authorization_cookies', 'rb')):
#         browser.driver.add_cookie(cookie)
#     time.sleep(5.0)
#     browser.driver.refresh()
#     time.sleep(10)


# @pytest.fixture()
# def authorized_cookie():
#     Token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9' \
#             '.eyJpc3MiOiJodHRwczovL2FwaS5lZGVtcmYuY29tIiwianRpIjoiYzRmZGJhMzQtNjYyMy00NWZkLWFkZWUtOWYzMjkyNmY0Yjc5IiwiaWF0IjoxNjk4MjQ0Mzk4LCJleHAiOjE3MDA4MzYzOTgsInVpZCI6MjU1MjQ0MSwicm9sZSI6InVzZXIifQ.WO6RDt-tWMgjlfjnJONKcN3qC_r0UmY7dZMvMNZnoD0&EIO=3&transport=polling&t=OjdGH4v'
#     response = requests.get(
#         url=base_url,
#         params={'Authorization': f'Bearer {Token}'}
#     )
#     authorization_cookie = response.text
#
#     yield authorization_cookie
#     time.sleep(5)


# @pytest.fixture()
# def authorized_cookie():
#     Token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9' \
#             '.eyJpc3MiOiJodHRwczovL2FwaS5lZGVtcmYuY29tIiwianRpIjoiYzRmZGJhMzQtNjYyMy00NWZkLWFkZWUtOWYzMjkyNmY0Yjc5IiwiaWF0IjoxNjk4MjQ0Mzk4LCJleHAiOjE3MDA4MzYzOTgsInVpZCI6MjU1MjQ0MSwicm9sZSI6InVzZXIifQ.WO6RDt-tWMgjlfjnJONKcN3qC_r0UmY7dZMvMNZnoD0&EIO=3&transport=polling&t=OjdGH4v'
#     head = {'Authorization': f'Bearer {Token}'}
#     response = requests.get(url='https://xn--d1abb2a.xn--p1ai/users/id2552441', headers=head)
#     # authorization_cookie = response.cookies.get("auth_token")
#     # browser.driver.add_cookie({"name": "auth_token", "value": authorization_cookie})
#     print(response.text)
# @pytest.fixture()
# def auth_jwt_token():
#     headers = {
#         'Authorization': f'Bearer {jwt_token}'
#     }
#     response = requests.get(base_url, headers=headers)
#     assert response.status_code == 200
#     assert response.json() == {'message': 'Success'}
