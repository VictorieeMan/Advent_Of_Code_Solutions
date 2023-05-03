"""Created: 2023-05-02, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/6
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

def parse_instruction_to_command(input_line):
    """Three type pf strings:
    turn off 301,3 through 808,453
    turn on 351,678 through 951,908
    toggle 720,196 through 897,994

    Parse to list on the form: [#1 verb,x1,y1,x2,y2]
    #1; 0:off, 1:on, 2:toggle

    Call that list a command
    """
    str_list = input_line.split() #split on each space " "
    list_tail = str_list[-3:] #irrespective of verb, tails are the same.

    #Add verb command list
    command = []
    if(str_list[0]=="toggle"):
        command += [2]
    elif(str_list[1]=="off"):
        command += [0]
    elif(str_list[1]=="on"):
        command += [1]
    
    #Add coordinates to command list
    command += [int(x) for x in list_tail[0].split(',')]
    command += [int(x) for x in list_tail[2].split(',')]

    return command

    

    

def partOne(input):
    command = parse_instruction_to_command(input[0])
    print(command)
	
### Part 2 ###
def partTwo(input):
    pass

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = input.split("\n")
partOne(input)
partTwo(input)