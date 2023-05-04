"""Created: 2023-05-04, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/7
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

def convert_if_int(string):
    try:
        return int(string)
    except:
        return string

def parsing_couplings(coupling, circuit_board):
    """Storing couplings in dictionary.
    Using coupling output as keys,
    and as dictionary values either their direct integer signal
    or coupling instructions as an array.

    key: 'Value/Instruction'
    """
    array = coupling.split()
    array_length = len(array)
    if array_length == 3:
        circuit_board[array[-1]] = convert_if_int(array[0])
    else:
        array[0] = convert_if_int(array[0])
        array[2] = convert_if_int(array[2])
        circuit_board[array[-1]] = array[0:-2]

#Bitwise operations
def AND(a,b):
    return a&b

def OR(a,b):
    return a|b

def LSHIFT(a,b):
    return a<<b

def RSHIFT(a,b):
    return a>>b

def NOT(a):
    return 65535-a

def check_int(test):
    return isinstance(test,int)

def check_str(test):
    return isinstance(test,str)

#Recursive calculation of circuit board
def fetch_and_operate(target,board):
    """On successful evaluation the board is also dynamically update,
    to save computing power and not having to redo recursive tracks.
    """
    # print(target) #Good print for debug
    if check_int(target):
        return target
    elif check_int(board[target]):
        return board[target]
    elif check_str(board[target]):
        return fetch_and_operate(board[target],board)
    else:
        if board[target][0] == 'NOT':
            a = fetch_and_operate(board[target][1],board)
            ans = NOT(a)
            board[target] = ans
            return ans
        
        else:
            a = fetch_and_operate(board[target][0],board)
            if board[target][1] == 'AND':
                b = fetch_and_operate(board[target][2],board)
                ans = AND(a,b)
                board[target] = ans
                return ans
            
            elif board[target][1] == 'OR':
                b = fetch_and_operate(board[target][2],board)
                ans = OR(a,b)
                board[target] = ans
                return ans
            
            elif board[target][1] == 'LSHIFT':
                b = board[target][2]
                ans = LSHIFT(a,b)
                board[target] = ans
                return ans
            
            elif board[target][1] == 'RSHIFT':
                b = board[target][2]
                ans = RSHIFT(a,b)
                board[target] = ans
                return ans

def partOne(input):
    board = {} #Build circuit board, store as dictionary.
    for coupling in input:
        if coupling == '':
            continue
        parsing_couplings(coupling, board)
    
    for target in board:
        signal = fetch_and_operate(target,board)
        print(target,': ',signal)
    
    a = fetch_and_operate('a',board)
    print('Part 1:',a)
    return a
	
### Part 2 ###
def partTwo(input, a):
    board = {}
    for coupling in input:
        if coupling == '':
            continue
        parsing_couplings(coupling, board)
    
    board['b'] = a
    
    a = fetch_and_operate('a',board)
    print('Part 2:',a)
    

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = input.split('\n')
a = partOne(input)
partTwo(input, a)