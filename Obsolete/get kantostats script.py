k = open("pokedata.txt", 'r+');
for line in k:
    if "baseStats" in line:
        with open("AllStats.txt", 'a') as s:
            s.write(line);
