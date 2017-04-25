#   This program allows the user to input their Pokemon.
#   It will use the Pokemon's base stats as well as its level to calculate the Pokemon's stats.
#   The program will store all of the user's submitted Pokemon in a text file that can be read or written to by this program.

from math import floor;
import json;

class Pokemon(object):
    def __init__(self, number, name, level, moves, stats):
        self.number = number;
        self.name = name;
        self.level = level;
        self.moves = moves;
        self.stats = stats;

    def append_pokemon(self):
        with open("POKELIST.txt", 'a') as p:
            p.write("%s | %s\nLevel %s\nHP: %s | Atk: %s | Def: %s | SpA: %s | SpD: %s | Spe: %s\n- %s\n- %s\n- %s\n- %s\n\n" % \
                    (self.number, self.name, self.level, self.stats[0], self.stats[1], self.stats[2], self.stats[3], \
                     self.stats[4], self.stats[5], self.moves[0], self.moves[1], self.moves[2], self.moves[3]));

def from_number_find_name(number):
    with open("AllPokemon.txt", 'r') as k:
        for i, line in enumerate(k, start = 1):
            if i == number:
                return line;

def from_name_find_number(name):
    with open("AllPokemon.txt", 'r') as k:
        for i, line in enumerate(k, start = 1):
            if line.rstrip('\n') == name:
                return i;

def from_number_find_stats(number):
    with open("kantostats.txt", 'r') as k:
        for i, line in enumerate(k, start = 1):
            if i == number:
                return line;

def convert_string_to_list(base_stats):
    base_stats = base_stats.rstrip('\n');
    l = base_stats.split('|');
    k = []
    for i in l:
        k.append(int(i));
    return(k);

def calculate_stats(base_stats, level):
    stats = [0] * 6
    for i in range(len(base_stats)):
        stats[i] = floor(((((2 * base_stats[i] + 31 + 0) * level) / 100) + 5) * 1);
    stats[0] = floor((((2 * base_stats[0] + 31 + 0) * level) / 100) + level + 10);
    return stats;

def parse_lines(num_and_name, level, stats, move1, move2, move3, move4):
    num_name_list = num_and_name.split(" | ");
    number = int(num_name_list[0]);
    name = num_name_list[1].rstrip('\n');
    level = int(level.lstrip("Level "));
    stats = stats.replace("HP: ", '');
    stats = stats.replace(" | Atk: ", ", ");
    stats = stats.replace(" | Def: ", ", ");
    stats = stats.replace(" | SpA: ", ", ");
    stats = stats.replace(" | SpD: ", ", ");
    stats = stats.replace(" | Spe: ", ", ");
    stats = stats.split(',');
    new_stats = [];
    for i in stats:
        new_stats.append(int(i));
    move1 = move1.replace("- ", '').rstrip('\n');
    move2 = move2.replace("- ", '').rstrip('\n');
    move3 = move3.replace("- ", '').rstrip('\n');
    move4 = move4.replace("- ", '').rstrip('\n');
    moves = [move1, move2, move3, move4];
    Poke = Pokemon(number, name, level, moves, new_stats);
    return Poke;

def choice():
    while True:
        answer = input("Would you like to view, modify, or create Pokemon?: ").lower();
        if answer == 'view' or answer == 'v' or answer == '1':
            view_mode();
        elif answer == 'modify' or answer == 'm' or answer == '2':
            modify_mode();
        elif answer == 'create' or answer == 'c' or answer == '3':
            create_mode();
        elif answer == 'q' or answer == 'quit':
            quit();
        else:
            print("That's not a valid input.");

############################
# create mode              #
############################

def create_mode():
    while True:
        name = input("Enter the name of the Pokemon you'd like to add: ").title();
        if name == 'Q' or name == 'Quit':
            choice();
        with open("AllPokemon.txt", 'r') as p:
            for line in p:
                if name == line.rstrip('\n'):
                    New_Poke = create_pokemon(name);
                    New_Poke.append_pokemon();
                    run_again();
            print("That's not the name of a Pokemon!");

def create_pokemon(name):
    number = from_name_find_number(name);
    base_stats = from_number_find_stats(number);
    base_stats = convert_string_to_list(base_stats);
    level = input("What level is the Pokemon?: ");
    while is_100_int(level) == False:
        print("The level must be between 1 and 100.");
        level = input("What level is the Pokemon?: ");
    level = int(level);
    #yn = input("Would you like to input EVs, IVs, both, or neither? If 'neither' is selected, IVs of 31 and EVs of 0 will be used: ");
    #if yn == 
    stats = calculate_stats(base_stats, level);
    moves = [''] * 4;
    moves[0] = input("What is the Pokemon's first move?: ").title();
    moves[1] = input("What is the Pokemon's second move?: ").title();
    moves[2] = input("What is the Pokemon's third move?: ").title();
    moves[3] = input("What is the Pokemon's fourth move?: ").title();
    New_Poke = Pokemon(number, name, level, moves, stats);
    return New_Poke;

############################
# modify mode              #
############################

def modify_mode():
    while True:
        slot = input("Which slot would you like to modify?: ");
        if slot.lower() == 'q' or slot.lower() == "quit":
            choice();
        if is_pos_int(slot) == True:
            slot = int(slot);
            if exists(slot) == False:
                print("That slot does not yet exist. You will be redirected to create mode.");
                create_mode();
            else:
                modify_slot(slot);
        else:
            print("Please input a positive integer.");

def modify_slot(slot):
    slot_line = 8 * (slot - 1);
    with open("POKELIST.txt", 'r') as p:
        for i, line in enumerate(p):
            if i == slot_line:
                num_and_name = line;
            elif i == slot_line + 1:
                level = line;
            elif i == slot_line + 2:
                stats = line;
            elif i == slot_line + 3:
                move1 = line;
            elif i == slot_line + 4:
                move2 = line;
            elif i == slot_line + 5:
                move3 = line;
            elif i == slot_line + 6:
                move4 = line;
    Poke = parse_lines(num_and_name, level, stats, move1, move2, move3, move4);
    while True:
        new = input("What aspect would you like to modify? You may modify the Pokemon, the level, or the moves: ").lower();
        if new == 'p' or new == 'pokemon' or new == '1':
            Poke = modify_pokemon(Poke);
            Poke.append_pokemon();
            run_again();
        elif new == 'l' or new == 'level' or new == '2':
            Poke = modify_level(Poke);
            Poke.append_pokemon();
            run_again();
        elif new == 'm' or new == 'moves' or new == '3':
            Poke = modify_moves(Poke);
            Poke.append_pokemon();
            run_again();
        else:
            print("Please enter either 'Pokemon', 'level', or 'moves'.");
            
def modify_pokemon(Poke):
    while True:
        name = input("Enter the name of the Pokemon you'd like to add: ").title();
        with open("AllPokemon.txt", 'r') as p:
            for line in p:
                if name == line.rstrip('\n'):
                    Poke.name = name;
                    Poke.number = from_name_find_number(Poke.name);
                    base_stats = from_number_find_stats(Poke.number);
                    base_stats = convert_string_to_list(base_stats);
                    Poke.stats = calculate_stats(base_stats, Poke.level);
                    return Poke;
        print("That's not the name of a Pokemon!");

def modify_level(Poke):
    level = input("What would you like to change the level to?: ");
    while is_100_int(level) == False:
        print("The level must be between 1 and 100.");
        level = input("What level is the Pokemon?: ");
    level = int(level);
    Poke.level = level;
    base_stats = from_number_find_stats(Poke.number);
    base_stats = convert_string_to_list(base_stats);
    Poke.stats = calculate_stats(base_stats, Poke.level);
    return Poke;

def modify_moves(Poke):
    Poke.moves = [''] * 4;
    Poke.moves[0] = input("What is the Pokemon's first move?: ").title();
    Poke.moves[1] = input("What is the Pokemon's second move?: ").title();
    Poke.moves[2] = input("What is the Pokemon's third move?: ").title();
    Poke.moves[3] = input("What is the Pokemon's fourth move?: ").title();
    return Poke;

############################
# view mode                #
############################

def view_mode():
    while True:
        slot = input("Which slot would you like to view?: ");
        if slot.lower() == 'q' or slot.lower() == "quit":
            choice();
        while True:
            if is_pos_int(slot) != True:
                print("Please input a positive integer.");
                slot = input("Which slot would you like to view?: ");
            else:
                slot = int(slot);
                break;
        if exists(slot) == True:
            view_slot(int(slot));
        else:
            print("That slot doesn't exist!");

def view_slot(slot):
    slot_line = 10 * (slot - 1);
    with open("POKELIST.txt", 'r') as p:
        for i, line in enumerate(p):
            if i >= slot_line and i <= slot_line + 9:
                print(line, end = '');
    run_again();

############################
# utility functions        #
############################

def is_pos_int(num):
    try:
        num = int(num);
        if num >= 1:
            return True;
        else:
            return False;
    except ValueError:
        return False;

def is_100_int(num):
    try:
        num = int(num);
        if num >= 1 and num <= 100:
            return True;
        else:
            return False;
    except ValueError:
        return False;

def exists(slot):
    with open("POKELIST.txt", 'r') as p:
        slot_line = 8 * (slot - 1);
        for i, line in enumerate(p):
            if i > slot_line:
                return True;
        return False;

def run_again():
    while True:
        ans = input("Would you like to run the program again?: ").lower();
        if ans == 'y' or ans == 'yes':
            choice();
        elif ans == 'n' or ans == 'no':
            quit();
        else:
            print("Please answer with either 'yes' or 'no'.");

############################
# main() and function body #
############################

def main():
    choice();

main();


##def change_pokemon(Poke, slot_line):
##    with open("POKELIST.txt", 'ab+') as p:
##        for i, line in enumerate(p):
##            if i == slot_line:
##                p.write("%s | %s\nLevel %s\nHP: %s | Atk: %s | Def: %s | SpA: %s | SpD: %s | Spe: %s\n- %s\n- %s\n- %s\n- %s\n\n" % \
##                    (self.number, self.name, self.level, self.stats[0], self.stats[1], self.stats[2], self.stats[3], \
##                     self.stats[4], self.stats[5], self.moves[0], self.moves[1], self.moves[2], self.moves[3]));
##def make_kanto_dex():
##    kanto_dex_list = []
##    with open("Kanto with quotes.txt", 'r', encoding = "utf8") as k:
##        for line in k:
##            kanto_dex_list.append(line);
##    kanto_dex = "".join(kanto_dex_list).splitlines();
