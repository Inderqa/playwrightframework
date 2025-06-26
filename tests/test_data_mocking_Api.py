import responses
import requests

@responses.activate
def test_api():
    responses.add(
        responses.GET,
        'https://api.example.com/user',
        json={'name': 'Cheetah', 'role': 'QA'},
        status=200
    )

    resp = requests.get('https://api.example.com/user')
    print(resp.json())  # {'name': 'Cheetah', 'role': 'QA'}