k = open("kantodata.txt", 'r+');
for line in k:
    print(line);
    if "baseStats" in line:
        with open("kantostats.txt", 'a') as s:
            s.write(line);
