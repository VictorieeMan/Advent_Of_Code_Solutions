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

class GuestPreferences:
    def __init__(self):
        self.pref = {}
    
    def add_pref(self, personA, personB, value):
        if personA not in self.pref:
            self.pref[personA] = {}
        self.pref[personA][personB] = value
    
    def get_pref(self, personA, personB):
        if personA in self.pref:
            if personB in self.pref[personA]:
                # This is how personA values the company of personB
                return self.pref[personA][personB]
            else:
                # If person B is missing, then personA is indifferent to them.
                return 0
        else:
            # If person A is missing, then personA is indifferent to everyone.
            return 0
    
    def get_mutual_pref(self, personA, personB):
        """Returns the sum of the mutual opinion of company."""
        return self.get_pref(personA, personB) + self.get_pref(personB, personA)

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
    guest_pref = GuestPreferences()
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
        
        # This is how personA values the company of personB
        # guest_pref[personA][personB] = value
        guest_pref.add_pref(personA, personB, value)
    
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

def finding_happiest_table_value(guest_pref, guest_idx, pos_placements):
    """Searching for the happiest talbe, by testing all permutations."""

    # Creating a reverse dict of guest_idx, for faster lookup.
    idx_guest = {}
    for guest,idx in guest_idx.items():
        idx_guest[idx] = guest

    def mutual_mood(persA_idx, persB_idx):
        """Given two people, return the sum of their mutual opinion of company."""
        persA = idx_guest[persA_idx]
        persB = idx_guest[persB_idx]

        # Adding their opinion of the others company together.
        sum = guest_pref.get_mutual_pref(persA, persB)
        
        return sum
    
    max_table_value = 0
    num_guests = len(guest_idx)
    for placement in pos_placements:
        sum = 0
        #Calculating the sum mood of the current placement.
        for i in range(num_guests):
            #Picking people pairwise around the table, with current placement.
            idx_A = i
            idx_B = (i+1) % num_guests #Because they are sitting in a circle

            persA_idx = placement[idx_A]
            persB_idx = placement[idx_B]
            sum += mutual_mood(persA_idx, persB_idx)
        
        if sum > max_table_value:
            max_table_value = sum

    return max_table_value

def partOne(input):
    data = parsing_input(input)
    guest_idx, guest_pref = structuring_data(data)
    placement = creating_placement_array(guest_idx)
    possible_placements = at.permutations(placement)
    max_table_value = finding_happiest_table_value(
        guest_pref, guest_idx, possible_placements
        )
    print(max_table_value)
    print("Part 1, Done!\n")
    return guest_idx, guest_pref
	
### Part 2 ###
def partTwo(guest_idx, guest_pref):

    # Adding myself ot the guest list
    idx = len(guest_idx)
    guest_idx["Mr. Me"] = idx

    # Same as the rest of partOne()
    placement = creating_placement_array(guest_idx)
    possible_placements = at.permutations(placement)
    max_table_value = finding_happiest_table_value(
        guest_pref, guest_idx, possible_placements
        )
    print(max_table_value)
    print("Part 2, Done!\n")

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = input.split('\n')[:-1] #Skipping last line, that's usually empty.
guest_idx, guest_pref = partOne(input)
partTwo(guest_idx, guest_pref)