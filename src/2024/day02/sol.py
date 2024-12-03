import pyperclip
import sys

from src.input_reader import read_input_lines

def part1(reports):
    # brute force solution since I want to get this in before EOD
    safe_reports = []
    for i, report in enumerate(reports):
        if is_safe(report):
            safe_reports.append(i)
    num_safe = len(safe_reports)
    print(f'num safe reports: {num_safe}')
    return num_safe
    
def is_safe(report):
    # not optimal, but gets the job done
    diffs = [i - j for i, j in zip(report, report[1:])]
    return diff_checks(diffs)

def diff_checks(diffs):
    strictly_monotonic = all([diff > 0 for diff in diffs]) or all([diff < 0 for diff in diffs])
    if not strictly_monotonic:
        return False
    jump_range = (1, 3) # inclusive, ie 1, 2, 3
    only_small_jumps = all([jump_range[0] <= abs(diff) <= jump_range[1] for diff in diffs])
    return only_small_jumps

def part2(reports):
    # again, brute force
    safe_dampened_reports = []
    for i, report in enumerate(reports):
        if is_safe_dampened(report):
            safe_dampened_reports.append(i)
    num_safe_dampened = len(safe_dampened_reports)
    print(f'num safe dampened reports: {num_safe_dampened}')
    return num_safe_dampened

def is_safe_dampened(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True
    return False

    # failed attempt at a smarter solution
    # diffs = [i - j for i, j in zip(report, report[1:])]
    # pos_diffs = [diff > 0 for diff in diffs]
    # if pos_diffs.count(True) == len(pos_diffs) - 1:
    #     idx = pos_diffs.index(False)
    # elif pos_diffs.count(False) == len(pos_diffs) - 1:
    #     idx = pos_diffs.index(True)
    # else:
    #     return False
    # # slice elt from report and check diffs
    # if idx > 0 and diff_checks(diffs[:max(idx-2, 0)] + [diffs[idx-1] + diffs[idx]] + diffs[idx:]):
    #     print()
    #     print(diffs)
    #     print(diffs[:max(idx-2, 0)] + [diffs[idx-1] + diffs[idx]] + diffs[idx:])
    #     return True
    # if idx < len(diffs) - 1 and diff_checks(diffs[:max(idx-1, 0)] + [diffs[idx] + diffs[idx+1]] + diffs[idx+1:]):
    #     print()
    #     print(diffs)
    #     print(diffs[:max(idx-1, 0)] + [diffs[idx] + diffs[idx+1]] + diffs[idx+1:])
    #     return True
    # return False

if __name__ == "__main__":
    # reports are strings that contain numbers separated by spaces
    reports = read_input_lines()
    reports = [list(map(int, report.split())) for report in reports]
    sol1 = part1(reports)
    sol2 = part2(reports)
    copy_part = sys.argv[1] if len(sys.argv) > 1 else "2" if sol2 else "1"
    pyperclip.copy(sol1 if copy_part == "1" else sol2)