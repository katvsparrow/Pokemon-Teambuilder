pokemon = [];
with open("pokedex.txt", "r+", encoding = "utf8") as alola:
    for line in alola:
        pokemon.append('"' + line[:len(line) - 1] + '"');

with open("pokedex.txt", 'w', encoding = "utf8") as new_alola:
    new_alola.write("\n".join(pokemon));
