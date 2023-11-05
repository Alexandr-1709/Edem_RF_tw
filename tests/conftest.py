import pytest
from selene.support.shared import browser
from edem_rf.model.data.data_for_tests import base_url
from edem_rf.utils import attach
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def driver_management_remote():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        keep_alive=True,
        options=options,
    )

    browser.config.driver = driver
    browser.config.hold_driver_at_exit = False
    browser.config.base_url = base_url
    browser.config.window_width = 1150
    browser.config.window_height = 800
    browser.config.timeout = 5.0

    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


