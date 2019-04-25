import os
import pytest

"""Configuration for pytest runner."""
import allure
from allure_commons.types import AttachmentType
from pyautomation.drivers.web_drivers import WebDrivers

def pytest_addoption(parser):
    parser.addoption("--config", action="store")
    parser.addoption("--browser", action="store")
         
@pytest.fixture(scope='session', autouse=True)
def config(request):
    config_file = request.config.option.config
    if config_file and os.path.isfile(config_file):
        os.environ['AUTO_CONFIG'] = config_file
        print("-- overriding default configuration with : " + config_file)
    else:
        print("Config file doesn't exist")

@pytest.fixture(scope="function")
def browser(request):
    return WebDrivers.get()
    
@pytest.fixture(scope="session", autouse=True)
def set_browser(request):
    browser = request.config.option.browser
    if browser:
        os.environ["CORE.DRIVER"] = browser
        print("-- overriding default driver configuration with : " + browser)

# Reporting attach screenshot when test fails
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        try:
            _driver = item.cls.driver
        except Exception:
            _driver = item.funcargs.get('browser', None)
        # if not exception
        else:
            if report.when == "call":
                extra.append(pytest_html.extras.url(_driver.current_url))
            if report.when == 'call' or report.when == "setup":
                xfail = hasattr(report, 'wasxfail')
                # Go to screenshot only when UI tests
                if (report.skipped and xfail) or (report.failed and not xfail):
                    url = _driver.current_url
                    extra.append(pytest_html.extras.url(url))
                    screenshot = _driver.get_screenshot_as_base64()
                    extra.append(pytest_html.extras.image(screenshot, ''))
                    allure.attach('screenshot', _driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    report.extra = extra
    
# Runs after complete session
def pytest_sessionfinish(session, exitstatus):
    pass
    
def pytest_unconfigure(config):
    pass