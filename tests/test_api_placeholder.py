import pytest


@pytest.mark.parametrize('input_id, output_id',
                         [
                             (1, 1),
                             (100, 100)
                         ]
                         )
def test_api_posts(api_client, input_id, output_id):
    result = api_client.get(path="/posts", params={'id': input_id}).json()
    assert result[0]['id'] == output_id


@pytest.mark.parametrize('input_name, output_email',
                         [
                             ("et omnis dolorem", "Mallory_Kunze@marie.org"),
                             ("alias odio sit", "Lew@alysha.tv")
                         ]
                         )
def test_api_comments(api_client, input_name, output_email):
    result = api_client.get(path="/comments", params={'name': input_name}).json()
    assert result[0]['email'] == output_email


@pytest.mark.parametrize('input_id, output_completed',
                         [
                             (4, True),
                             (5, False)
                         ])
def test_api_todos(api_client, input_id, output_completed):
    result = api_client.get(path="/todos", params={'id': input_id}).json()
    assert result[0]['completed'] == output_completed


def test_api_albums(api_client):
    result = api_client.post(path="/comments",
                             data={'title': "qui fuga est a eum"}
                             ).json()
    assert result['id'] == 501


def test_api_photos(api_client):
    result = api_client.get(path="/photos",
                             params={'id': 5}
                             ).json()
    assert result[0]['title'] == "natus nisi omnis corporis facere molestiae rerum in"
