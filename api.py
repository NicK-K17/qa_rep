import requests

def all_posts():
    # response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert len(response.json()) == 100, 'Not all post returned'  #

def one_post():
    post_id = new_post()
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.json()['id'] == post_id # сравнивает вернулся ли юзер с тем id который запрашивался
    print(response.text)

def post_a_post():
    body = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    assert response.status_code == 201, 'Status code is incorrect'
    assert response.json()['id'] == 101, 'ID is incorrect'

def new_post():
    body = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
    return response.json()['id']

def clear(post_id):
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

def put_a_post():
    post_id = new_post()
    body = {
        "title": "Test Title - UPD",
        "body": "Test Body - UPD",
        "userId": 1
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=body, headers=headers)
    assert response.json()['title'] == 'Test Title - UPD'
    clear(post_id)


def patch_a_post():
    post_id = new_post()
    body = {
        "title": "Test Title - UPD2",
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=body, headers=headers)
    print(response.text)
    clear(post_id)


def delete_a_post():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/24')
    print(response.text)

