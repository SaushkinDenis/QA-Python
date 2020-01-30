import pytest


@pytest.mark.parametrize('input_par', ["", "1", "0", "51"])
def test_api_with_params(api_client, input_par):
    result = api_client.get(path="/breeds/image/random/{}".format(input_par)).json()
    assert result["status"] == "success"
    assert result["message"] is not None


@pytest.mark.parametrize('input_par', ["blood", "basset", "english"])
def test_api_random_dogs(api_client, input_par):
    result = api_client.get(path="/breed/hound/{}/images/random".format(input_par)).json()
    assert result["status"] == "success"
    assert type(result["message"]) == str


def test_api_random_dog(api_client):
    result = api_client.get(path="/breeds/image/random").json()
    assert result["status"] == "success"
    assert result["message"] is not None


def test_api_all_breeds(api_client):
    result = api_client.get(path="/breeds/list/all").json()
    assert result["status"] == "success"
    assert type(result["message"]) == dict
    assert "affenpinscher" in result["message"]


def test_api_out_image(api_client):
    result = api_client.get(path="/breed/hound/images").json()
    assert result["message"][0].split(".")[3] == "jpg"
