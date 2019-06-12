import requests
def poke_gallery():
    url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    r = requests.get(url)
    data = r.json().get('pokemon')
    fi = open("pokemon.html", "w")
    for pokemon in data:
        fi.write('<img src = '+ pokemon["img"] + ' height = "100px" width = "100px">')
    fi.close()

# poke_gallery()