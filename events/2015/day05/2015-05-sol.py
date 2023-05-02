"""Created: 2023-05-02, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/5
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

import re

def three_vowels_check(string):
    vowels = "aeiou"
    counter = 0

    for char in string:
        if(char in vowels):
            counter +=1
            if counter == 3:
                return True
    
    return False

def double_letter_check(string):
    for i in range(0,len(string)-1):
        if(string[i]==string[i+1]):
            return True
        
    return False

def no_forbidden_check(string):
    forbidden_pairs = ["ab","cd","pq","xy"]
    for pair in forbidden_pairs:
        if re.search(pair,string):
            return False
        
    return True

def check_for_nice(string):
    if double_letter_check(string):
        if three_vowels_check(string):
            if no_forbidden_check(string):
                return 1
    return 0

def partOne(input):
    data = input.split("\n")
    nice = 0
    for string in data:
        nice += check_for_nice(string)
    print(nice)

	
### Part 2 ###
def check_for_two_letterPairs(string):
    last_char = len(string) - 1
    i = 0
    while i <= last_char-3: #Shortest potential string is 4 long.
        pair = string[i:i+2] #iterating over pairs in the string.
        string_tail = string[i+2:]
        if re.search(pair,string_tail): #Checking for second occurance.
            return True
        i += 1
    
    return False

def check_for_letterSandwich(string):
    # Check for triple with begin = end, ex: xyx
    triple = ["","",""] #Implemented as a que; first in, first out
    for char in string:
        triple.append(char)
        triple.pop(0)
        if(triple[0]==triple[-1]):
            return True
    return False


def check_for_nice_2(string):
    if check_for_letterSandwich(string):
        if check_for_two_letterPairs(string): #The more expensive funciton
            return True
        
    return False
        

def partTwo(input):
    data = input.split("\n")
    nice = 0
    for string in data:
        nice += check_for_nice_2(string)
    print(nice)

### Main ###
input = at.input_to_string(__file__,"input.txt")
partOne(input)
partTwo(input)