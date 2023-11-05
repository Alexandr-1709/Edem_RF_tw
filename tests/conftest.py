import pytest
from selene.support.shared import browser
from edem_rf.model.data.data_for_tests import base_url
from edem_rf.utils import attach


@pytest.fixture(scope='function', autouse=True)
def driver_management_remote():
    browser.config.base_url = base_url
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 5.0

    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()


