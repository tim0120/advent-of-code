import re

import numpy as np

from utils.copy import copy_sol
from utils.inputs import read_input_lines

def part1(lines, grid, query):
    horizontal_matches = get_all_horizontal(lines, query)
    vertical_matches = get_all_vertical(grid, query)
    diagonal_matches = get_all_diagonal(grid, query)
    print(f"matches: {horizontal_matches + vertical_matches + diagonal_matches}")
    return horizontal_matches + vertical_matches + diagonal_matches
    

def get_all_horizontal(lines, query):
    pattern = r'(?=({0}|{1}))'.format(query, query[::-1])
    matches = sum([
        len(re.findall(pattern, line)) for line in lines
    ])
    return matches

def get_all_vertical(grid, query):
    query_inv = query[::-1]
    length = len(query)
    matches = 0
    for i in range(len(grid) - length + 1):
        for j in range(len(grid[0])):
            test = ''.join(grid[i:i+length, j].flatten())
            if test == query or test == query_inv:
                matches += 1
    return matches

def get_all_diagonal(grid, query):
    query_inv = query[::-1]
    length = len(query)
    matches = 0
    for i in range(len(grid) - length + 1):
        # backslash diagonal
        for j in range(len(grid[0]) - length + 1):
            test = ''.join(grid[i+k, j+k] for k in range(length))
            if test == query or test == query_inv:
                matches += 1
        # forward slash diagonal
        for j in range(length - 1, len(grid[0])):
            test = ''.join(grid[i+k, j-k] for k in range(length))
            if test == query or test == query_inv:
                matches += 1
    return matches

def part2(grid, query):
    matches = get_all_crosses(grid, query)
    print(f"matches: {matches}")
    return matches

def get_all_crosses(grid, query):
    query_inv = query[::-1]
    length = len(query)
    matches = 0
    for i in range(len(grid) - length + 1):
        # backslash diagonal
        for j in range(len(grid[0]) - length + 1):
            test1 = ''.join(grid[i+k, j+k] for k in range(length))
            test2 = ''.join(grid[i+k, j+length-1-k] for k in range(length))
            if (test1 == query or test1 == query_inv) and (test2 == query or test2 == query_inv):
                matches += 1
    return matches

if __name__ == "__main__":
    lines = read_input_lines()
    query1 = 'XMAS'
    query2 = 'MAS'
    grid = np.array([
        [i for i in line]
        for line in lines
    ])
    sol1 = part1(lines, grid, query1)
    sol2 = part2(grid, query2)
    copy_sol(sol1, sol2)