import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="Request URL")
    parser.addoption("--status_code", action="store", default=None, help="Request status")


@pytest.fixture(scope="session")
def api_client(request):
    urls = {
        "dog": "https://dog.ceo/api",
        "brewery": "https://api.openbrewerydb.org",
        "placeholder": "https://jsonplaceholder.typicode.com",
        "ya.ru": "https://ya.ru"
    }

    init = request.config.getoption("--url")
    if init in urls:
        base_url = urls.get(init)
    else:
        base_url = init

    base_status = request.config.getoption("--status_code")
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
