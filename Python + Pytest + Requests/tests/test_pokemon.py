import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"

@pytest.mark.parametrize("key, value", [("trainer_name", "NikitaT")])
def test_trainer_name(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers?trainer_id=13088')
    assert response_parametrize.json()["data"][0][key] == value    

@pytest.mark.parametrize("endpoint, status_code", [
    ("/trainers", 200)
])
def test_status_code(endpoint, status_code):
    response = requests.get(url=f"{URL}{endpoint}")
    assert response.status_code == status_code