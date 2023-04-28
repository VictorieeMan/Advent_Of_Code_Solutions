"""Created: 2023-04-28, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions

Purpose: A collection of tools for the Advent of Code 2015 solutions.
"""
import os

### Utility ###

def get_ScriptDir(FILE):
    """Returns the directory of the script that calls this function."""
    script_path = os.path.realpath(FILE)
    script_dir = os.path.dirname(script_path)
    return script_dir

def get_InputPath(FILE,filename="input.txt"):
    """Returns the path to the input.txt file in the same directory as the script that calls this function."""
    script_dir = get_ScriptDir(FILE)
    input_path = os.path.join(script_dir, filename)
    return input_path

def input_to_string(FILE,filename):
    """Reads the input from the file with the given filename,
    and returns it as a string."""
    with open(get_InputPath(FILE,filename), 'r') as file:
        input_string = file.read()
    return input_string

### Classes ###

class Coordinate_2d(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Coordinate_2d(self.x + other.x, self.y + other.y)
    
    """"""
    # Added to make the class iterable and possible to store in a set.
    def __hash__(self) -> int:
        return hash((self.getX(), self.getY()))
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Coordinate_2d):
            return self.getX() == other.getX() and self.getY() == other.getY()
        return False
    """"""
    
    def getX(self):
        """Good for reducing Encapsulation 'leaky abstraction',
        Read-Only access & scalability. We can now centrally change how out xy,
        is stored within this class without disturbing code that calls .getX
        """
        # Get method for X coordinate
        return self.x
    
    def getY(self):
        # Get method for Y coordinate
        return self.y
    
    def tuple_out(self):
        """Returns a coordinate tuple
        """
        return tuple((self.getX(),self.getY()))


### Functions ###

### Math