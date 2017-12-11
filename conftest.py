import pytest
from connection import Connection

driver = Connection.driver

@pytest.fixture()
def reset_url():
    driver.delete_all_cookies()
    driver.get("https://test-z5y5zwrh0g.hub3c.com/")
    print("Reset URL")

