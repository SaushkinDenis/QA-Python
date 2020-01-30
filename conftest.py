import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="Request URL")
    parser.addoption("--status_code", action="store", default="", help="Request status")


@pytest.fixture(scope="session")
def api_client(request):
    if request.config.getoption("--url") == "dog":
        base_url = "https://dog.ceo/api"
    elif request.config.getoption("--url") == "brewery":
        base_url = "https://api.openbrewerydb.org"
    elif request.config.getoption("--url") == "placeholder":
        base_url = "https://jsonplaceholder.typicode.com"
    elif request.config.getoption("--url") == "ya.ru":
        base_url = "https://ya.ru"
    else:
        base_url = request.config.getoption('--url')

    if request.config.getoption("--status_code") != "":
        base_status = request.config.getoption("--status_code").split("=")[1]
    else:
        base_status = None
    return APIClient(base_url, base_status)


class APIClient:

    def __init__(self, base_address, status=None):
        self.base_address = base_address
        self.status = status

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        print("POST request to {}".format(url))
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        url = self.base_address + path
        print("GET request to {}".format(url))
        return requests.get(url=url, params=params)

    def get_status(self):
        return self.status
