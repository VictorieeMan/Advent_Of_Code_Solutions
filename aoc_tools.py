"""Created: 2023-04-28, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions

Purpose: A collection of tools for the Advent of Code solutions.
"""

def input_to_string(filename):
    """Reads the input from the file with the given filename,
    and returns it as a string."""
    with open(filename, 'r') as file:
        input_string = file.read()
    return input_string