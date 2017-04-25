from math import floor;
import json;

with open("pokedata.json", 'r') as dt:
    pokedex = json.load(dt);

class Pokemon(object):
    def __init__(self, number, species, ability, item, level, stats, moves):
        self.number = number;
        self.species = species;
        self.ability = ability;
        self.item = item;
        self.level = level;
        self.stats = stats;
        self.moves = moves;

    def append_pokemon(self):
        self.species = self.species.title();
        poke_as_text = "%s | %s\nAbility: %s\nItem: %s\nLevel %s\nHP: %s | Atk: %s | Def: %s | SpA: %s | SpD: %s | Spe: %s\n- %s\n- %s\n- %s\n- %s\n\n" % \
                    (self.number, self.species, self.ability, self.item, self.level, self.stats['hp'], self.stats['atk'], self.stats['def'], self.stats['spa'], \
                     self.stats['spd'], self.stats['spe'], self.moves[0], self.moves[1], self.moves[2], self.moves[3]);
        with open("POKELIST.txt", 'a') as p:
            p.write(poke_as_text);

def calculate_stats(baseStats, level, EVs, IVs, nature):
    nature_values = calc_nature(nature);
    stats = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0};
    stats["hp"] = floor((((2 * baseStats["hp"] + IVs["hp"] + EVs["hp"] / 4) * level) / 100) + level + 10);
    stats["atk"] = floor(((((2 * baseStats["atk"] + IVs["atk"] + EVs["atk"] / 4) * level) / 100) + 5) * nature_values["atk"]);
    stats["def"] = floor(((((2 * baseStats["def"] + IVs["def"] + EVs["def"] / 4) * level) / 100) + 5) * nature_values["def"]);
    stats["spa"] = floor(((((2 * baseStats["spa"] + IVs["spa"] + EVs["spa"] / 4) * level) / 100) + 5) * nature_values["spa"]);
    stats["spd"] = floor(((((2 * baseStats["spd"] + IVs["spd"] + EVs["spd"] / 4) * level) / 100) + 5) * nature_values["spd"]);
    stats["spe"] = floor(((((2 * baseStats["spe"] + IVs["spe"] + EVs["spe"] / 4) * level) / 100) + 5) * nature_values["spe"]);
    return stats;

def calc_nature(nature):
    nature_values = {"hp": 1, "atk": 1, "def": 1, "spa": 1, "spd": 1, "spe": 1};
    if nature == "Quirky" or nature == "Hardy" or nature == "Bashful" or nature == "Docile" or nature == "Serious":
        return nature_values;
    elif nature == "Lonely":
        nature_values["atk"] = 1.1;
        nature_values["def"] = 0.9;
    elif nature == "Adamant":
        nature_values["atk"] = 1.1;
        nature_values["spa"] = 0.9;
    elif nature == "Naughty":
        nature_values["atk"] = 1.1;
        nature_values["spd"] = 0.9;
    elif nature == "Brave":
        nature_values["atk"] = 1.1;
        nature_values["spe"] = 0.9;
    elif nature == "Bold":
        nature_values["def"] = 1.1;
        nature_values["atk"] = 0.9;
    elif nature == "Impish":
        nature_values["def"] = 1.1;
        nature_values["spa"] = 0.9;
    elif nature == "Lax":
        nature_values["def"] = 1.1;
        nature_values["spd"] = 0.9;
    elif nature == "Relaxed":
        nature_values["def"] = 1.1;
        nature_values["spe"] = 0.9;
    elif nature == "Modest":
        nature_values["spa"] = 1.1;
        nature_values["atk"] = 0.9;
    elif nature == "Mild":
        nature_values["spa"] = 1.1;
        nature_values["def"] = 0.9;
    elif nature == "Rash":
        nature_values["spa"] = 1.1;
        nature_values["spd"] = 0.9;
    elif nature == "Quiet":
        nature_values["spa"] = 1.1;
        nature_values["spe"] = 0.9;
    elif nature == "Calm":
        nature_values["spd"] = 1.1;
        nature_values["atk"] = 0.9;
    elif nature == "Gentle":
        nature_values["spd"] = 1.1;
        nature_values["def"] = 0.9;
    elif nature == "Careful":
        nature_values["spd"] = 1.1;
        nature_values["spa"] = 0.9;
    elif nature == "Sassy":
        nature_values["spd"] = 1.1;
        nature_values["spe"] = 0.9;
    elif nature == "Timid":
        nature_values["spe"] = 1.1;
        nature_values["atk"] = 0.9;
    elif nature == "Hasty":
        nature_values["spe"] = 1.1;
        nature_values["def"] = 0.9;
    elif nature == "Jolly":
        nature_values["spe"] = 1.1;
        nature_values["spa"] = 0.9;
    elif nature == "Naive":
        nature_values["spe"] = 1.1;
        nature_values["spd"] = 0.9;
    return nature_values;

def parse_lines(num_and_species, ability, item, level, stats, move1, move2, move3, move4):
    num_species_list = num_and_species.split(" | ");
    number = int(num_species_list[0]);
    species = num_species_list[1].rstrip('\n');
    ability = ability.lstrip("Ability: ");
    item = item.lstrip("Item: ");
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
    Poke = Pokemon(number, species, ability, item, level, new_stats, moves);
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
        species = input("Enter the name of the Pokemon you'd like to add: ").lower();
        if species == 'Q' or species == 'Quit':
            choice();
        while species in pokedex:
            New_Poke = create_pokemon(species);
            New_Poke.append_pokemon();
            run_again();
        print("That's not the name of a Pokemon!");

def create_pokemon(species):
    number = pokedex[species]["num"];
    nature_list = ["Hardy", "Serious", "Bashful", "Quirky", "Docile", \
                   "Lonely", "Adamant", "Naughty", "Brave", \
                   "Bold", "Impish", "Lax", "Relaxed", \
                   "Modest", "Mild", "Rash", "Quiet", \
                   "Calm", "Gentle", "Careful", "Sassy", \
                   "Timid", "Hasty", "Jolly", "Naive"];
    while True:
        print("Which ability does your Pokemon have?\n1: %s" % (pokedex[species]["abilities"]["0"]));
        poss_abilities = ability_exist(pokedex[species]["abilities"]);
        if poss_abilities == "1" or poss_abilities == "1H":
            print("2: " + pokedex[species]["abilities"]["1"]);
        if poss_abilities == "H" or poss_abilities == "1H":
            print("H: " + pokedex[species]["abilities"]["H"]);
        ability = input("Choice: ");
        if ability == "1":
            ability = pokedex[species]["abilities"]["0"];
            break;
        elif (poss_abilities == "1" and ability == "2") or (poss_abilities == "1H" and ability == "2"):
            ability = pokedex[species]["abilities"]["1"];
            break;
        elif (poss_abilities == "H" or poss_abilities == "h" and (ability == "H" or ability == "h")) or (poss_abilities == "1H" and (ability == "H" or ability == "h")):
            ability = pokedex[species]["abilities"]["H"];
            break;
        else:
            print("Please enter the number of an ability that appears above.");            
    level = input("What level is the Pokemon?: ");
    while is_100_int(level) == False:
        print("The level must be between 1 and 100.");
        level = input("What level is the Pokemon?: ");
    level = int(level);
    while True:
        yn = input("Would you like to input EVs, IVs, both, or neither? If 'neither' is selected, IVs of 31 and EVs of 0 will be used: ").upper();
        if yn == '1' or yn == 'E' or yn == 'EV' or yn == 'EVS':
            IVs = {"hp": 31, "atk": 31, "def": 31, "spa": 31, "spd": 31, "spe": 31};
            EVs = get_EV();
            break;
        elif yn == '2' or yn == 'I' or yn == 'IV' or yn == 'IVS':
            EVs = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0};
            IVs = get_IV();
            break;
        elif yn == '3' or yn == 'BOTH' or yn == 'B':
            EVs = get_EV();
            IVs = get_IV();
            break;
        elif yn == '4' or yn == 'NEITHER' or yn == 'N':
            EVs = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0};
            IVs = {"hp": 31, "atk": 31, "def": 31, "spa": 31, "spd": 31, "spe": 31};
            break;
        else:
            print("That is not a valid input.");
    while True:
        nature = input("What nature would you like to use? If you would not like to enter a nature, type 'none': ").title();
        if nature == "None":
            nature = "Hardy";
            break;
        elif nature in nature_list:
            break;
        elif nature not in nature_list and nature != "None":
            print("That is not a valid nature.");
    stats = calculate_stats(pokedex[species]["baseStats"], level, EVs, IVs, nature);
    moves = [''] * 4;
    moves[0] = input("What is the Pokemon's first move?: ").title();
    moves[1] = input("What is the Pokemon's second move?: ").title();
    moves[2] = input("What is the Pokemon's third move?: ").title();
    moves[3] = input("What is the Pokemon's fourth move?: ").title();
    item = choose_item();
    New_Poke = Pokemon(number, species, ability, item, level, stats, moves);
    return New_Poke;

def choose_item():
    return "Leftovers";

def get_IV():
    print("\nInput the IVs of your Pokemon. Keep in mind that IVs must be between 0 and 31.");
    IVs = {"hp" : 0, "atk" : 0, "def" : 0, "spa" : 0, "spd" : 0, "spe" : 0};
    IV_names = ["hp", "atk", "def", "spa", "spd", "spe"];
    translate = {"hp" : "HP IV: ", "atk" : "Attack IV: ", "def" : "Defense IV: ", "spa" : "Special Attack IV: ", "spd" : "Special Defense IV: ", "spe" : "Speed IV: "};
    for value in IV_names:
        while True:
            IVs[value] = input(translate[value]);
            if is_valid_IV(IVs[value]) == False:
                print("That's not a valid value. Please enter a value between 0 and 31.");
            elif is_valid_IV(IVs[value]) == True:
                IVs[value] = int(IVs[value]);
                break;
    return IVs;

def get_EV():
    print("\nInput the EVs of your Pokemon. Keep in mind that EVs must be between 0 and 255, and that the sum of all a Pokemon's EVs cannot exceed 510.");
    EVs = {"hp" : 0, "atk" : 0, "def" : 0, "spa" : 0, "spd" : 0, "spe" : 0};
    EV_names = ["hp", "atk", "def", "spa", "spd", "spe"];
    translate = {"hp" : "HP IV: ", "atk" : "Attack IV: ", "def" : "Defense IV: ", "spa" : "Special Attack IV: ", "spd" : "Special Defense IV: ", "spe" : "Speed IV: "};
    while True:
        total = 0;
        for value in EV_names:
            while True:
                EVs[value] = input(translate[value]);
                if is_valid_EV(EVs[value]) == False:
                    print("That's not a valid value. Please enter a value between 0 and 255.");
                elif is_valid_EV(EVs[value]) == True:
                    EVs[value] = int(EVs[value]);
                    total += EVs[value];
                    break;
        if total > 510:
            print("The total value of the Pokemon's EVs exceeds 510. Please input them again.");
        elif total <= 510:
            break;
    return EVs;

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
    slot_line = 10 * (slot - 1);
    with open("POKELIST.txt", 'r') as p:
        for i, line in enumerate(p):
            if i == slot_line:
                num_and_name = line;
            elif i == slot_line + 1:
                ability = line;
            elif i == slot_line + 2:
                item = line;
            elif i == slot_line + 3:
                level = line;
            elif i == slot_line + 4:
                stats = line;
            elif i == slot_line + 5:
                move1 = line;
            elif i == slot_line + 6:
                move2 = line;
            elif i == slot_line + 7:
                move3 = line;
            elif i == slot_line + 8:
                move4 = line;
    Poke = parse_lines(num_and_name, ability, item, level, stats, move1, move2, move3, move4);
    while True:
        new = input("What aspect would you like to modify? You may modify the Pokemon, the level, the moves, the ability, the nature, the EVs, or the IVs: ").lower();
        if new == 'p' or new == 'pokemon' or new == '1':
            Poke = modify_pokemon(Poke);
        elif new == 'l' or new == 'level' or new == '2':
            Poke = modify_level(Poke);
        elif new == 'm' or new == 'moves' or new == '3':
            Poke = modify_moves(Poke);
        elif new == 'a' or new == 'ability' or new == '4':
            Poke = modify_ability(Poke);
        elif new == 'n' or new == 'nature' or new == '5':
            Poke = modify_nature(Poke);
        elif new == 'e' or new == 'evs' or new == '6':
            Poke = modify_EVs(Poke);
        elif new == 'i' or new == 'ivs' or new == '7':
            Poke = modify_IVs(Poke);
        else:
            print("Please enter either 'Pokemon', 'level', 'moves', 'ability', 'nature', 'EVs', or 'IVs'.");
        Poke.append_pokemon();
        run_again();
            
def modify_pokemon(Poke):
    while True:
        name = input("Enter the name of the Pokemon you'd like to add: ").lower();
        if name in pokedex:
            Poke = create_pokemon(name);
            return Poke;
        print("That's not the name of a Pokemon!");

def modify_level(Poke):
    level = input("What would you like to change the level to?: ");
    while is_100_int(level) == False:
        print("The level must be between 1 and 100.");
        level = input("What level is the Pokemon?: ");
    level = int(level);
    Poke.level = level;
    
    Poke.stats = calculate_stats(base_stats, Poke.level);
    return Poke;

def modify_moves(Poke):
    Poke.moves = [''] * 4;
    Poke.moves[0] = input("What is the Pokemon's first move?: ").title();
    Poke.moves[1] = input("What is the Pokemon's second move?: ").title();
    Poke.moves[2] = input("What is the Pokemon's third move?: ").title();
    Poke.moves[3] = input("What is the Pokemon's fourth move?: ").title();
    return Poke;

def modify_nature(Poke):
    nature_list = ["Hardy", "Serious", "Bashful", "Quirky", "Docile", \
                   "Lonely", "Adamant", "Naughty", "Brave", \
                   "Bold", "Impish", "Lax", "Relaxed", \
                   "Modest", "Mild", "Rash", "Quiet", \
                   "Calm", "Gentle", "Careful", "Sassy", \
                   "Timid", "Hasty", "Jolly", "Naive"];
    while True:
        Poke.nature = input("What nature would you like to use? If you would not like to enter a nature, type 'none': ").title();
        if Poke.nature == "None":
            Poke.nature = "Hardy";
            break;
        elif Poke.nature in nature_list:
            break;
        elif Poke.nature not in nature_list and nature != "None":
            print("That is not a valid nature.");
    

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

def exists(slot):
    with open("POKELIST.txt", 'r') as p:
        slot_line = 10 * (slot - 1);
        for i, line in enumerate(p):
            if i > slot_line:
                return True;
        return False;

############################
# utility functions        #
############################

def ability_exist(abilities):
    num_ability = [];
    for ability in abilities:
        num_ability.append(ability);
    i = len(num_ability);
    if i == 1:
        return "0";
    elif i == 3:
        return "1H";
    elif i == 2:
        if "H" in num_ability:
            return "H";
        elif "1" in num_ability:
            return "1"; 

def is_100_int(num):
    try:
        num = int(num);
        if num >= 1 and num <= 100:
            return True;
        else:
            return False;
    except ValueError:
        return False;

def is_pos_int(num):
    try:
        num = int(num);
        if num >= 1:
            return True;
        else:
            return False;
    except ValueError:
        return False;

def is_pos_int_or_0(num):
    try:
        num = int(num);
        if num >= 0:
            return True;
        else:
            return False;
    except ValueError:
        return False;

def is_valid_IV(IV):
    if is_pos_int_or_0(IV) == False:
        return False;
    IV = int(IV);
    if IV < 0 or IV > 31:
        return False;
    return True;

def is_valid_EV(EV):
    if is_pos_int_or_0(EV) == False:
        return False;
    EV = int(EV);
    if EV < 0 or EV > 255:
        return False;
    return True;

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
# main and body            #
############################

def main():
    choice();

main();
