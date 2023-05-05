"""Created: 2023-05-05, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/12
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

def convert_char_digit_array_to_int(digit_array):
    """Assumes input of an array like this ['2','5'] and
    converts it to integer 25
    """
    if digit_array: #If non empty
        number = ''.join(digit_array)
        number = int(number)
    else:
        number = 0
    return number

def partOne(input):
    array = list(input)
    i = 0
    sum = 0
    number = []
    last_found = -1
    for char in array:
        if char.isdigit():
            if array[i-1] == '-':
                char = '-' + char
            if last_found == i-1:
                number += [char]
            else:
                digit = convert_char_digit_array_to_int(number)
                sum += digit
                number = []
                number += [char]
            last_found = i
        i += 1
    digit = convert_char_digit_array_to_int(number)
    sum += digit
    print(sum)
    print("Part 1, Done!\n")
	
### Part 2 ###
def partTwo(input):
    """Ignore any object (and all of its children) which has any property with
    the value "red". Do this only for objects ({...}), not arrays ([...]).
    """
    print("Part 2, Done!\n")

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = input[:-1] #Skipping last char \n
partOne(input)
partTwo(input)