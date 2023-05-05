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

def look_and_say(string):
    """Preforms the iterative action of counting according to
    the rules of the game.
    """
    new_string = [] #Adding to list was much faster than concatenating  strings.
    length = len(string)
    i = 0
    while i < length:
        char = string[i]

        #Count continious occurances of char
        count = 1
        char_i = char
        while i+1 < length and char_i == string[i+1]:
            count += 1
            i += 1
            if string[i+1] == None:
                break
        new_string.append(str(count))
        new_string.append(char)
        i += 1
    return ''.join(new_string)
        

def partOne(input):
    string = input
    for i in range(40):
        string = look_and_say(string)
    print(len(string))
    print("Part 1, Done!\n")
	
### Part 2 ###
def partTwo(input):
    print("Part 2, Done!\n")

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = input[:-1] #Skipping last char, that's a newline char.
partOne(input)
partTwo(input)