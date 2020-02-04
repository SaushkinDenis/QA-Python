import pytest


@pytest.mark.parametrize('input_city, input_state, input_number, output_country',
                         [
                             ("San Diego", "California", 88588882188, "United States")
                         ])
def test_api_country(api_client, input_city, input_state, input_number, output_country):
    result = api_client.get(path="/breweries",
                            params={
                                 "phone": input_number,
                                 "city": input_city,
                                 "state": input_state
                             }).json()
    assert result[0]["country"] == output_country


@pytest.mark.parametrize('input_city, output_city', [("san_diego", "San Diego")])
def test_api_filter_by_city(api_client, input_city, output_city):
    result = api_client.get(path="/breweries", params={"by_city": input_city}).json()
    assert result[0]["city"] == output_city


@pytest.mark.parametrize('input_city, output_name', [("eppig_brewing", "Eppig Brewing")])
def test_api_by_name(api_client, input_city, output_name):
    result = api_client.get(path="/breweries", params={"by_name": input_city}).json()
    assert result[0]["name"] == output_name


@pytest.mark.parametrize('input_tag', ["tours"])
def test_api_by_tag(api_client, input_tag):
    result = api_client.get(path="/breweries", params={"by_tag": input_tag}).json()
    assert result == []


@pytest.mark.parametrize('input_key, output_state', [("city", "Pennsylvania")])
def test_api_sort_by_city(api_client, input_key, output_state):
    result = api_client.get(path="/breweries", params={"sort": input_key}).json()
    assert result[0]["state"] == output_state
