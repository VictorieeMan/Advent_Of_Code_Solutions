"""Created: 2023-04-28, by @VictorieeMan
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

def dir_addition(position, dir):
    """This funciton adds the direction to a coordinate.
    """
    if (dir == "<"):
        position += at.Coordinate_2d(-1,0)
    elif (dir == "^"):
        position += at.Coordinate_2d(0,1)
    elif (dir == ">"):
        position += at.Coordinate_2d(1,0)
    elif (dir == "v"):
        position += at.Coordinate_2d(0,-1)

    return position

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
        position = dir_addition(position, dir)
        visited.add(position)
        # print(position.tuple_out())
    
    print(len(visited))
	
### Part 2 ###
def partTwo(input):
    """Data contains directional steps,
    how many unique points are visited in the discretky defined grid?
    """
    position = at.Coordinate_2d(0,0)
    santa_pos = position
    rob_pos = position
    iterator = 0

    visited = set()
    visited.add(position)

    # This for loop "walks" around the grid, but this time we iterate between
    # santa_pos and rob_pos. Letting them take their own steps.
    for dir in input:
        if (iterator % 2 == 0):
            santa_pos = dir_addition(santa_pos, dir)
            position = santa_pos
        elif (iterator % 2 == 1):
            rob_pos = dir_addition(rob_pos, dir)
            position = rob_pos
        visited.add(position)
        iterator += 1
        # print(position.tuple_out())
    
    print(len(visited))

### Main ###
input = at.input_to_string(__file__,"input.txt")
partOne(input)
partTwo(input)