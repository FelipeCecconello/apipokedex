import requests
import json

with open("pokedex.json") as lista_pokemons:
    database = json.load(lista_pokemons)

for n in range (151):
    dados = requests.get(database[n]['url'])
    json_dados = dados.json()

    database[n]['id'] = json_dados['id']
    database[n]['foto'] = json_dados['sprites']['front_default']
    database[n]['habilidades'] = json_dados['abilities']
    database[n]['propriedades'] = json_dados['stats']
    database[n]['tipos'] = json_dados['types']


with open('database.json', 'w') as file:
    json.dump(database, file, indent=2)