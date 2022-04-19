# apipokedex
API de pokedex

Pré-requisitos
  Necessário a bilbioteca Flask para iniciar a API, a biblioteca pode ser instalada com o comando "pip install flask"
  
Documentação
  A API foi desenvolvida em python com o framework flask.
  Atualmente possui 2 endpoints com a database dos 151 primeiros pokemons, um para listar os pokemons e outro para listar um pokemon de maneira detalhada.
  
  1. Listagem dos Pokémons
    Exemplos de utilização para a listagem dos pokemons, podendo utilizar ou não a variavel limit para limitar a exibição.
    GET .../pokemon/
    GET .../pokemon/&limit=151
    
 2. Detalhes do Pokemon
    Exemplos utilização para a listagem detalhada do pokemon, podendo utilizar o id ou nome do pokemon.
    GET .../pokemon/{id ou nome}
    GET .../pokemon/1
    GET .../pokemon/bulbasaur
    
 
 
    
