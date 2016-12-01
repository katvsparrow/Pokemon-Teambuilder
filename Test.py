import json

with open('pokedata.json', 'r') as dt:
    dex = json.load(dt);
    print(dex["bulbasaur"]);
    print(dex["bulbasaur"]["baseStats"]);
