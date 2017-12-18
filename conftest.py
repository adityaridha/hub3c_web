import pytest
from connection import Connection

driver = Connection.driver

@pytest.fixture()
def reset_url():
    driver.delete_all_cookies()
    driver.get("https://test-z5y5zwrh0g.hub3c.com/")
    print("Reset URL")

@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            driver.get_screenshot_as_file(file_name)


