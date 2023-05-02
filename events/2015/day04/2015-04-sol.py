"""Created: 2023-, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/4
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

import hashlib

def leading_zeros_check(string,quantity=5):
    try:
        for i in range(0,quantity):
            if(string[i] != '0'):
                return False
    except:
        #In case of errors, return False. Ex, string to short.
        return False
    return True
            

def partOne(input,quantity=5):
    key = input.split("\n")[0] # To exlude the newline char.
    number = 1
    str2hash = key + str(number)
    hash = hashlib.md5(str2hash.encode()).hexdigest()

    while not leading_zeros_check(hash,quantity):
        number += 1
        str2hash = key + str(number)
        hash = hashlib.md5(str2hash.encode()).hexdigest()
    
    print(number)
        
	
### Part 2 ###
def partTwo(input):
    partOne(input,6)

### Main ###
input = at.input_to_string(__file__,"input.txt")
partOne(input)
partTwo(input)