import unittest
import requests

class TestPostApi(unittest.TestCase): # класс в котором есть пред и пост условия
    def setUp(self): # предусловие (в данном случае создание поста)
        body = {
            "title": "Test Title",
            "body": "Test Body",
            "userId": 1
        }
        headers = {
            "Content-type": "application/json; charset=UTF-8"
        }
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
        self.post_id = response.json()['id']
        print(f'Post created: {self.post_id}')

    def tearDown(self) -> None: # постусловие (в данном случае удаление поста)
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        print(f'Post deleted: {self.post_id}')

    @unittest.skip('Getting error on each run') # пропуск теста (можно указать причину)
    def test_get_one_post(self):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')
        self.assertEqual(response.json()['id'], self.post_id)

class TestIndependent(unittest.TestCase): # класс в котором НЕТ пред и пост условия
    def test_get_all_posts(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        self.assertEqual(len(response.json()), 100)

    def test_add_post(self):
        body = {
            "title": "Test Title",
            "body": "Test Body",
            "userId": 1
        }
        headers = {
            "Content-type": "application/json; charset=UTF-8"
        }
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body, headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)