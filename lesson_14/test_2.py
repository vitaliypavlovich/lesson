import requests

if __name__ == '__main__':
    response = requests.post('http://127.0.0.1:5000', data={
   "email": "test@test",
    'password': 'test-password'
})

    assert response.status_code == 200