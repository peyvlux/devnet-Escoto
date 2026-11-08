import random
import requests

POKEMON_LIST = ["pikachu", "bulbasaur", "charizard", "greninja", "lucario"]


def fetch_pokemon_data(pokemon_name):
    """Fetches Pokémon data from PokeAPI with error handling."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Error: Pokémon '{pokemon_name}' not found.")
            return None
        else:
            print("Game Over!")
            print("Pokemon was :", answer)
            return None
    except requests.exceptions.RequestException as e:
        print("Could not get the pokemon")
        return None