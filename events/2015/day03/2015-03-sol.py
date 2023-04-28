"""Created: 2023-, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/3
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
    """Data contains directional steps,
    how many unique points are visited in the discretky defined grid?
    """
    position = at.Coordinate_2d(0,0)

    visited = set()
    visited.add(position)

    # This for loop "walks" around the grid,
    # and adds each position to a set that only keeps unique positions.
    for dir in input:
        if (dir == "<"):
            position += at.Coordinate_2d(-1,0)
        elif (dir == "^"):
            position += at.Coordinate_2d(0,1)
        elif (dir == ">"):
            position += at.Coordinate_2d(1,0)
        elif (dir == "v"):
            position += at.Coordinate_2d(0,-1)
        visited.add(position)
        print(position.tuple_out())
    
    print(len(visited))
	
### Part 2 ###
def partTwo(input):
    pass

### Main ###
input = at.input_to_string(__file__,"input.txt")
partOne(input)
partTwo(input)