"""Created: 2023-08-07, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/13
"""
# For importing the aoc_tools.py file
import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
del directory # Removing variable, for a cleaner debug

import aoc2015_tools as at
### START SOLUTION BODY ###
### Part 1 ###

def parsing_input(input):
    """Input: list of strings"""
    """Sample:
    "Alice would gain 2 happiness units by sitting next to Bob."
    "Alice would lose 82 happiness units by sitting next to David."
    After split() to a list, interesting data is indexed at [0,2,3,10]
    Note: that last element at index 10 also contains the name and a "."
    """
    data = []
    for str in input:
        str = str.split()
        data.append([str[0],str[2],str[3],str[10][:-1]])
        # ['Alice', 'gain', '2', 'Bob']
    return data

def structuring_data(data):
    """input: list of lists of strings"""
    """Converting the relational datapoints to directional edges,
    and adding them to a dictionary."""
    guests = set()
    guest_pref = {}
    for record in data:
        personA = record[0]
        mood    = record[1]
        points  = record[2]
        personB = record[3]

        # Converting opinion strings, to integer value
        value = int(points)
        if mood == "gain":
            value *= 1
        else:
            value *= -1

        if personA not in guests:
            # Adding guest to guest list
            guests.add(personA)
            # Creating the internal dictionary
            guest_pref[personA] = {}
        
        # This is how personA values the company of personB
        guest_pref[personA][personB] = value
    
    idx = 0
    guest_idx = {}
    for guest in guests:
        guest_idx[guest] = idx
        idx += 1

    return (guest_idx, guest_pref)

def creating_placement_array(guest_idx):
    """input: dictionary["guest_name"] = int(id)"""
    """To be easier on the memory when calculating permutations."""
    placement_array = []
    for guest, idx in guest_idx.items():
        placement_array.append(idx)
    
    return placement_array

def partOne(input):
    data = parsing_input(input)
    guest_idx, guest_pref = structuring_data(data)
    placement = creating_placement_array(guest_idx)
    possible_placements = at.permutations(placement)
    # happiest_table_value = max_talbe_value(possible_placements)
    print("Part 1, Done!\n")
	
### Part 2 ###
def partTwo(input):
    print("Part 2, Done!\n")

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = input.split('\n')[:-1] #Skipping last line, that's usually empty.
partOne(input)
# partTwo(input)