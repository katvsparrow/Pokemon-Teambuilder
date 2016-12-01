import json
pokedex = {}
with open('pokedata.json') as file:
   temp = json.load(file)
   for key, value in temp.items():
       if 'prevo' in value:
           pokedex[value['species']] = temp[value['prevo']]['species']
