"""Created: 2023-04-28, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/2
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

def extract_dimensions(package):
    """Extracts and sorts dimensions of each packages.
    The sorted order of the data is later used to make calculations efficient.
    """
    dim = package.split("x")    # Put values into a list of dimensions.
    dim = list(map(int, dim))   # Converts all strings to integers.
    dim.sort()                  # Sorts with smallest value first.

    return dim

def partOne(input):
    """Calculate the total surface area of all the packages.
    Needed per present: Surface area plus the area of the smallest side.
    """
    packages = input.split("\n")
    sq_totals=0
    for package in packages:
        if package: # Empty strings are registered as false.
            l,w,h = extract_dimensions(package)
            sq_totals += 3*l*w + 2*w*h + 2*h*l
    
    print(sq_totals)
	
### Part 2 ###
def partTwo(input):
    """Calculate the total length of ribbon needed for all the packages.
    Needed per present: Shortest perimiter + the volume of the package
    """
    packages = input.split("\n")
    total_len = 0
    for package in packages:
        if package:
            l,w,h = extract_dimensions(package)
            total_len += 2*(l+w)    # The shortest perimiter.
            total_len += l*w*h      # The volume of the box.

    print(total_len)

### Main ###
input = at.input_to_string(__file__,"input.txt")
partOne(input)
partTwo(input)