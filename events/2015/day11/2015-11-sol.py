"""Created: 2023-, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/11
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

def increment_password(password):
    """Increments password one setp.
    """
    for i in range(len(password)-1,-1,-1):
        if password[i] == 25:
            password[i] = 0
        else:
            password[i] += 1
            break
    return password

def check_and_fix_forbidden_chars(password,forbidden):
    """Check if password contains forbidden chars and fix if any.
    """
    for i in range(len(password)):
        if password[i] in forbidden:
            password[i] += 1 #Increment to next letter
            for j in range(i+1,len(password)):
                #Set all following letters to 0:'a'
                password[j] = 0

def check_for_triple_consecutive_letters(password):
    """Check if password contains triple consecutive letters,
    ex. 'abc' or 'xyz'. At least one tirple is required.
    """
    for i in range(len(password)-2):
        if password[i] == password[i+1]-1 and password[i] == password[i+2]-2:
            return True
    return False

def check_for_two_seperate_letter_pairs(password):
    """Looking for two non overlapping pairs of letters in the string,
    ex. aa and aa or xx and yy
    """
    count = 0
    skip = None
    for i in range(len(password)-1):
        if i != skip and password[i] == password[i+1]:
            count += 1
            skip = i + 1
            if count == 2:
                return True
            
    return False


def partOne(input):
    alphabet = dict(zip(range(26),"abcdefghijklmnopqrstuvwxyz"))
    alphanum = dict(zip("abcdefghijklmnopqrstuvwxyz",range(26)))
    #Converting input to a list of numbers
    password = [alphanum[letter] for letter in input]

    #Storing forbidden chars
    forbidden = [alphanum[letter] for letter in "iol"]

    #Find the next valid password
    while True:
        increment_password(password)
        #Check if password is valid
        check_and_fix_forbidden_chars(password,forbidden)
        if check_for_triple_consecutive_letters(password):
            if check_for_two_seperate_letter_pairs(password):
                break
         
    print(password)

    #Converting password numbers to a list of chars
    password = [alphabet[numb] for numb in password]
    password = ''.join(password)
    print(password)

    return password
	
### Part 2 ###
def partTwo(input):
    partOne(input)
    print("Part 2, Done!\n")

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = list(input[:-1]) #Input to char list.
password2 = partOne(input)
print("Part 1, Done!\n")
partTwo(password2)