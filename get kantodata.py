##def file_len(fname):
##    with open(fname) as f:
##        for i, l in enumerate(f):
##            pass
##    return i + 1

with open("pokedata.txt", 'r', encoding = "utf8") as p:
    for i, line in enumerate(p):
        with open("kantodata.txt", 'a', encoding = "utf8") as k:
            if i < 2599:
                k.write(line);
