import pytest
import os
from connection import Connection

driver = Connection.driver

@pytest.fixture()
def reset_url():
    driver.get("https://test-z5y5zwrh0g.hub3c.com/")

