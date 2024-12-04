from collections import Counter
import pyperclip
import sys

from utils.inputs import read_input_lines

def part1(sorted_lists, copy=False):
    # take diffs
    diffs = [abs(i-j) for (i, j) in zip(sorted_lists[0], sorted_lists[1])]
    # sum diffs
    sum_diffs = sum(diffs)
    # profit
    print(sum_diffs)
    if copy:
        pyperclip.copy(str(sum_diffs))

def part2(sorted_lists, copy=True):
    # name lists
    indexing_list = sorted_lists[0]
    scoring_list = sorted_lists[1]
    index_counts = Counter(indexing_list)
    scoring_counts = Counter(scoring_list)
    # get similarity scores
    # similarity scores are calculated by taking the 
    similaity_scores = [
        el * index_counts[el] * scoring_counts[el]
        for el in indexing_list
    ]
    # profit
    total_score = sum(similaity_scores)
    print(total_score)
    if copy:
        pyperclip.copy(str(total_score))


def sort_lists():
    # make input lists into Nx2 list of lists with int elts
    input = [
        [int(el) for el in line.split(' ') if el]
        for line in read_input_lines()
    ]
    # transpose
    lists = list(map(list, zip(*input)))
    # sort
    sorted_lists = [sorted(sublist) for sublist in lists]
    return sorted_lists

if __name__ == "__main__":
    sorted_lists = sort_lists()
    copy_part = sys.argv[1] if len(sys.argv) > 1 else "2"
    part1(sorted_lists, copy=(copy_part == "1"))
    part2(sorted_lists, copy=(copy_part == "2"))