'''Написать тест с использованием pytest и requests, в котором:
Адрес сайта, имя пользователя и пароль хранятся в config.yaml
conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login с передачей параметров
“username" и "password" и возвращающей токен авторизации
Тест с использованием DDT проверяет наличие поста
с определенным заголовком в списке постов другого пользователя, для этого выполняется get запрос по адресу
https://test-stand.gb.ru/api/posts c хедером, содержащим токен авторизации в параметре "X-Auth-Token".
Для отображения постов другого пользователя передается "owner": "notMe".
http://restapi.adequateshop.com/api/authaccount/registration
http://restapi.adequateshop.com/api/authaccount/login'''


import requests

url = "https://test-stand.gb.ru/gateway/login"
login = "kitty89"
password = "61d96a3985"

result = requests.post(url=url, data={"username": login, "password": password})
token = result.json()["token"]

res_get = requests.get(url="https://test-stand.gb.ru/api/posts", headers={"X-Auth-Token": token}, params={"owner": "notMe"})
print(res_get)
print(res_get.json())
