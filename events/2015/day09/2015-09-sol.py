"""Created: 2023-, by @VictorieeMan
Repository url: https://github.com/VictorieeMan/Advent_Of_Code_Solutions
Event url: https://adventofcode.com/2015/day/9
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

def inputEdges_to_graph(input)->dict:
    """Takes the input and returns a graph in the form of a nested dictionary."""
    graph = {}
    graph['nodes'] = set()
    for distance_str in input:
        array = distance_str.split()

        #Add to nested dictionary
        if array[0] not in graph:
            graph[array[0]] = {}
        graph[array[0]][array[2]] = int(array[4])

        #Add to set of nodes
        graph['nodes'].add(array[0])
        graph['nodes'].add(array[2])
    
    return graph

def path_length(path:tuple,graph:dict)->int:
    """Returns the length of the path."""
    length = 0
    for i in range(len(path)-1):
        try:
            length += graph[path[i]][path[i+1]]
        except KeyError:
            length += graph[path[i+1]][path[i]]
    return length

def partOne(input):
    #Starting and End point must be different.
    #Must visit each location exactly once.
    #Find the shortest path.
    graph = inputEdges_to_graph(input)
    possible_paths = at.permutations(graph['nodes'])

    lengths = []
    for i in range(len(possible_paths)):
        length = path_length(possible_paths[i],graph)
        lengths.append(length)
    
    print(min(lengths))

    print("Part 1, Done!\n")
    return lengths
	
### Part 2 ###
def partTwo(input):
    print(max(input))
    print("Part 2, Done!\n")

### Main ###
input = at.input_to_string(__file__,"input.txt")
input = input.split('\n')[:-1] #Skipping last line, that's usually empty.
lengths = partOne(input)
partTwo(lengths)