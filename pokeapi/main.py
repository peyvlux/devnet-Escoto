import random
import requests
<<<<<<< HEAD

pokemon_list = ["pikachu", "bulbasaur", "charizard", "greninja", "lucario"]

answer = random.choice(pokemon_list)

url = "https://pokeapi.co/api/v2/pokemon/" + answer
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    height = data["height"] * 10
    weight = data["weight"] / 10

    print("POKEMON GUESSING GAME")
    print("Guess the Pokemon!")
    print("Height:", height, "cm")
    print("Weight:", weight, "kg")
    print("You have 3 attempts.")

    for attempt in range(3):
        guess = input("Enter Pokemon name: ")

        if guess == answer:
            print("Correct! You win!")
            break
        else:
            print("Wrong guess!")
=======
 
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
>>>>>>> a023d8e (Update files before push)
    else:
        print("Game Over!")
        print("Pokemon was :", answer)

else:
    print("Could not get the pokemon")
