# pytest -vs -- запуск тестов(-v - расширенный, -s - аечатать принты)
# что бы запустить тест с тегом нужно добавить -m, например pytest -vs -m smoke (запуститься все что с тегом smoke)
# если запустить pytest -vs -m 'not smoke' (запуститься все что НЕ с тегом smoke)

import pytest
import requests

@pytest.fixture() # создание фикстуры (по умолчанию scope='function' - фикстура работает в рамкох одной функции)
def new_post_id(): # функция предусловия
    body = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    post_id = response.json()['id']
    yield post_id
    print(' Deleting the post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

@pytest.fixture(scope='session') # начинает работать перед функцией в которой она вызвана и заканчивает после всех тестов (функций)
def hello():
    print('Hello')
    yield
    print('Bye')

@pytest.mark.smoke
def test_get_one_post(new_post_id, hello):
    print('test')
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}')
    assert response.json()['id'] == new_post_id

@pytest.mark.smoke
def test_get_all_posts(new_post_id):

    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert len(response.json()) == 100

@pytest.mark.smoke
def test_add_post():
    body = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    assert response.status_code == 201
    assert response.json()['id'] == 101

@pytest.mark.regression
def test_1():
    assert 1 == 1

@pytest.mark.parametrize('logins', ['', ' ', '(&(*^']) # запуск теста с различными параметрами
def test_2(logins):
    print(logins)
    assert 2 == 2

def test_3():
    assert 3 == 3

