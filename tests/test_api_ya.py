def test_status_on_ya(api_client):
    result = api_client.get(path="/1")
    status = api_client.get_status()
    assert result.status_code == status


