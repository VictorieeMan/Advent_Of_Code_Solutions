"""Created: 2023-05-04, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/8
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

def count_str_chars(string):
    count = -2 #Excluding the beginning and ending " marks
    length = len(string)
    count += length

    #Search for all backslashes
    backslash_pos = [i for i, c in enumerate(string) if c == '\\']

    if len(backslash_pos) > 0:
        i = 0
        while i <= max(backslash_pos):
            if i in backslash_pos:
                #Due to input data, i+1 will never be out of bounce.
                if string[i+1] == '\\' or string[i+1] == '\"':
                    #Either a backslash or double-quote plus it's escapesequence
                    #We subtract the double count of the escape sequence char.
                    count -= 1
                    i += 1
                elif string[i+1] == 'x':
                    #Signals a hexadecimal noted char
                    #ex. \x27 is four chars, but represents one char
                    #we correct for the +3 overcount in the totals.
                    count -= 3
            i += 1

    return count

def partOne(input):
    total_code_chars = 0
    total_str__chars = 0
    for line in input:
        total_code_chars += len(line)
        total_str__chars += count_str_chars(line)
        # print(len(line),count_str_chars(line))
    
    ans = total_code_chars - total_str__chars
    print(ans)

	
### Part 2 ###
def calc_enc_chars(string):
    count = 2 #Including an extra " on each end of the string.
    length = len(string)
    count += length

    for char in string:
        if char == '\"' or char == '\\':
            count += 1

    return count

def partTwo(input):
    total_code_chars = 0
    total_enc__chars = 0
    for line in input:
        total_code_chars += len(line)
        total_enc__chars += calc_enc_chars(line)
        # print(len(line),calc_enc_chars(line))
    
    ans = total_enc__chars - total_code_chars
    print(ans)

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = input.split('\n')[:-1] #Disregard last row, that is empty.
# partOne(input)
partTwo(input)