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

def summarize_numbers_in_string(string):
    array = list(string)
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
    return sum

def partOne(input):
    sum = summarize_numbers_in_string(input)
    print(sum)
    print("Part 1, Done!\n")
	
### Part 2 ###
def find_red_dictvalues(dict_item):
    """Returns True if any value in the dict_item is "red".
    """
    for key,value in dict_item.items():
        if value == "red":
            return True
    return False

def remove_dicts_with_value_red(data):
    """Recursively removes all dicts with value "red".
    """
    try:
        new_data = data.copy()
    except:
        #If not copyable, when at the bottom of the recursion
        new_data = data
    if isinstance(new_data, dict):
        if find_red_dictvalues(new_data):
            new_data = None
        else:
            for key,value in new_data.items():
                new_data[key] = remove_dicts_with_value_red(value)
    elif isinstance(new_data, list):
        for i in range(len(new_data)):
            new_data[i] = remove_dicts_with_value_red(new_data[i])
    return new_data

def partTwo(input):
    """Ignore any object (and all of its children) which has any property with
    the value "red". Do this only for objects ({...}), not arrays ([...]).
    """
    import json
    data = json.loads(input)
    data = remove_dicts_with_value_red(data)
    #Sereialize to string
    data = json.dumps(data)
    #Summarize numbers in string, using part 1 function
    sum = summarize_numbers_in_string(data)
    print(sum)
    print("Part 2, Done!\n")

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = input[:-1] #Skipping last char \n
partOne(input)
partTwo(input)