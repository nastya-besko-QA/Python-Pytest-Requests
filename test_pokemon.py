import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '90a56b263088fe65fb2d40f02ea221d2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '34737'

def test_status_code():
    response = requests.get(url = f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
