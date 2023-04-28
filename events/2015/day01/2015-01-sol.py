"""Created: 2023-04-28, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/1
"""
# For importing the aoc_tools.py file
import path
import sys
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
del directory # Removing variable, for a cleaner debug

import aoc2015_tools as at
### START SOLUTION BODY ###

directions = at.input_to_string(__file__,"input.txt")
floor = 0

for direction in directions:
    if (direction == '('):
        floor += 1
    elif (direction == ')'):
        floor -= 1

print(floor)

