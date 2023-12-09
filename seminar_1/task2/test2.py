import requests
import yaml

with open("config.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)


def test_get_token(get_token):
    response = requests.post(url=data["url"],
                             data={"username": data["login"], "password": data["password"]})
    res_token = response.json()["token"]
    assert response.status_code == 200
    assert res_token == get_token


def test_check_post(get_token, request_get):
    headers = {'X-Auth-Token': get_token}
    response = requests.get(data["url_get"], headers=headers, params={'owner': 'notMe'})
    posts = response.json()
    assert response.status_code == 200
    assert posts == request_get


def test_check_post_title(get_token):
    headers = {'X-Auth-Token': get_token}
    response = requests.post(url=data["url_post"], headers=headers,
                             params={"title": data["title"],
                                     "description": data["description"],
                                     "content": data["content"]})
    post_title = response.json()["title"]
    assert response.status_code == 200
    assert post_title == data["title"]


def test_check_post_2(get_token, request_post):
    headers = {'X-Auth-Token': get_token}
    response = requests.get(data["url_get"], headers=headers, params={'owner': 'Me'})
    posts = response.json()
    assert response.status_code == 200
    assert any(post["title"] == request_post for post in posts["data"])
