import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "TOKEN"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

pokemon_create = requests.post(url = f"{URL}/pokemons", headers = HEADER, json = body_create)
print(pokemon_create.json())

pokemon_id = pokemon_create.json()["id"]

change_name = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}
pokemon_change_name = requests.put(url = f"{URL}/pokemons", headers = HEADER, json = change_name )
print(pokemon_change_name.json())

add_pokeball = {
    "pokemon_id": pokemon_id
}

pokemon_add_pokeball = requests.post(url = f"{URL}/trainers/add_pokeball", headers = HEADER, json = add_pokeball )
print(pokemon_add_pokeball.json())