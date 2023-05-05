"""Created: 2023-05-05, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/10
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

def partOne(input):

    print("Part 1, Done!\n")
	
### Part 2 ###
def partTwo(input):
    print("Part 2, Done!\n")

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = input[:-1] #Skipping last char, that's a newline char.
partOne(input)
partTwo(input)