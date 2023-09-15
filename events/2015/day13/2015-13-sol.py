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
        data.append([str[0],str[2],str[3],str[10][:-1]]) # ['Alice', 'gain', '2', 'Bob']
    return data

def partOne(input):
    data = parsing_input(input)
    print(data)
    print("Part 1, Done!\n")
	
### Part 2 ###
def partTwo(input):
    print("Part 2, Done!\n")

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = input.split('\n')[:-1] #Skipping last line, that's usually empty.
partOne(input)
# partTwo(input)