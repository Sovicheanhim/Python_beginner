import requests, json

def poke_type(type):
    print(type)
    URL = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    try:
        r = requests.get(url = URL)
    except Exception as e:
        print(e)
    pokedex = r.json().get('pokemon')
    result = []
    for y in pokedex:
        if set(type) <= set(y['type']):
            result.append([(y['id'], y['name'])])

    return result

# print(poke_type(['Water', 'Psychic']))