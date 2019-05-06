import os
import pytest

"""Configuration for pytest runner."""
import allure
from allure_commons.types import AttachmentType
from pyautomation.configuration import CONFIG
from pyautomation.logger.logger import LOG
from selenium.common.exceptions import WebDriverException
import base64
# 
def pytest_addoption(parser):
    parser.addoption("--mobile_device", action='store')
#     parser.addoption("--config", action="store")
#     parser.addoption("--browser", action="store")
#          
# @pytest.fixture(scope='session', autouse=True)
# def config(request):
#     config_file = request.config.option.config
#     if config_file and os.path.isfile(config_file):
#         os.environ['AUTO_CONFIG'] = config_file
#         print("-- overriding default configuration with : " + config_file)
#     else:
#         print("Config file doesn't exist")
# 
# @pytest.fixture(scope="session")
# def browser(request):
#     return WebDrivers.get()
#     
# @pytest.fixture(scope="session", autouse=True)
# def set_browser(request):
#     browser = request.config.option.browser
#     if browser:
#         os.environ["CORE.DRIVER"] = browser
#         print("-- overriding default driver configuration with : " + browser)

@pytest.fixture(scope='session')
def mobile_device(request):
    browser = request.config.option.mobile_device
    if browser:
        os.environ["MOBILE.DEVICE"] = mobile_device
        print("-- overriding default mobile device configuration with : " + mobile_device)
        
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
            pass
        # if not exception
        else:
            try:
                if report.when == 'setup':
                    _driver.start_recording_screen()
                    LOG.info("Started screen recording")
            except:
                pass
            if report.when == 'call' or report.when == "setup":
                xfail = hasattr(report, 'wasxfail')
                # Go to screenshot only when UI tests
                if (report.skipped and xfail) or (report.failed and not xfail):
                    try:
                        _video = _driver.stop_recording_screen()
                        LOG.info("ended screen recording")
                        with open('D:\Workspace\test.mp4', 'wb') as f:
                            f.write(base64.b64decode(_video))
                        LOG.info("written to a file")
                        url = _driver.current_url
                        allure.attach(url, "Application url", AttachmentType.TEXT)
                        extra.append(pytest_html.extras.url(url))
                    except WebDriverException as e:
                        LOG.error('Not able to get screen-recording')
                        LOG.error(e.msg)
                    screenshot = _driver.get_screenshot_as_base64()
                    extra.append(pytest_html.extras.image(screenshot, ''))
                    allure.attach(_driver.get_screenshot_as_png(), 'Screen-shot', AttachmentType.PNG)
    report.extra = extra
    try:
        _driver.stop_recording_screen()
    except:
        pass
    
# Runs after complete session
def pytest_sessionfinish(session, exitstatus):
    pass
    
def pytest_unconfigure(config):
    pass