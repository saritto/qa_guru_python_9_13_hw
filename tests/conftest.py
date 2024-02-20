import pytest
from selene import browser
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_height = 720
    browser.config.window_width = 1280

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)

    browser.quit()
