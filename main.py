import requests

from tests.test_pokemon import TRAINER_ID, URL

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '90a56b263088fe65fb2d40f02ea221d2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "274518",
    "name": "Чижик",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "274518"
}

'''response_create = requests.post(url = f'{URL}pokemons', headers= HEADER, json = body_create)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

'''response_change = requests.put(url = f'{URL}pokemons', headers= HEADER, json = body_change)
print(response_change.text)'''

'''message = response_change.json()['message']
print(message)'''


response_catch = requests.post(url = f'{URL}trainers/add_pokeball', headers= HEADER, json = body_catch)
print(response_catch.text)

message = response_catch.json()['message']
print(message)


