"""Created: 2023-04-28, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions

Purpose: A collection of tools for the Advent of Code 2015 solutions.
"""
import os

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