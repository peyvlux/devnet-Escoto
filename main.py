import random
import requests

POKEMON_LIST = ["pikachu", "bulbasaur", "charizard", "greninja", "lucario"]

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"Error: Pokémon '{pokemon_name}' not found.")
            return None
        else:
            print(f"Error: Received unexpected status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Network connection failed - {e}.")
        return None

if __name__ == "__main__":
    print("Terminal setup test successful!")
