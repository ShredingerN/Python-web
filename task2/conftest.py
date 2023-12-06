import pytest
import requests
import yaml

with open('config.yaml', encoding="utf-8") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def get_token():
    result = requests.post(url=data["url"], data={"username": data["login"],
                                                  "password": data["password"]})
    token = result.json()["token"]
    return token


@pytest.fixture()
def request_get(get_token):
    res_get = requests.get(url=data["url_get"], headers={"X-Auth-Token": get_token},
                           params={"owner": "notMe"})
    return res_get.json()


@pytest.fixture()
def request_post(get_token):
    send_post = requests.post(url=data["url_post"], headers={"X-Auth-Token": get_token},
                              params={"title": data["title"],
                                      "description": data["description"],
                                      "content": data["content"]})
    post_title = send_post.json()["title"]
    return post_title
