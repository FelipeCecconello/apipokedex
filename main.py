from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/pokemon')
def lista_todos_pokemons():
    with open("pokedex.json") as lista_pokemons:
        database = json.load(lista_pokemons)

    return jsonify(database)

@app.route('/pokemon&limit=<int:limit>')
def lista_pokemons(limit):
    with open("pokedex.json") as lista_pokemons:
        database = json.load(lista_pokemons)

    response = []
    for n in range(limit):
        response.append(database[n])

    return jsonify(response)

@app.route('/pokemon/<int:id>')
def detalhes_pokemon_id(id):
    with open("database.json") as lista_pokemons:
        database = json.load(lista_pokemons)

    response = database[id-1]

    return jsonify(response)

@app.route('/pokemon/<string:name>')
def detalhes_pokemon_name(name):
    with open("database.json") as lista_pokemons:
        database = json.load(lista_pokemons)

    for n in range(151):
        if database[n]['name'] == name:
            index = n

    response = database[index]

    return jsonify(response)

app.run()