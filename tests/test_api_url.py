def test_status_on_url(api_client):
    result = api_client.get(path="")
    status = api_client.get_status()
    assert result.status_code == int(status)
