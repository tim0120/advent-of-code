import re
from typing import List

from utils.copy import copy_sol
from utils.inputs import read_input_lines

def part1(memory_lines: List[str]) -> int:
    memory = "".join(memory_lines)
    prod_sum = get_mul_sum(memory)
    print(f"sum of all muls: {prod_sum}")
    return prod_sum

def get_mul_sum(memory: str) -> int:
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    mul_instances = re.findall(mul_pattern, memory)
    products = [
        int(mul[0]) * int(mul[1])
        for mul in mul_instances
    ]
    return sum(products)

def part2(memory_lines) -> int:
    memory = "".join(memory_lines)
    # match don't() up until the next do() or end of string
    dont_keep_pattern = r"don't\(\).*?(do\(\)|$)"
    # remove such matches
    memory = re.sub(dont_keep_pattern, "", memory)
    prod_sum = get_mul_sum(memory)
    print(f"sum of all do muls: {prod_sum}")
    return prod_sum

if __name__ == "__main__":
    memory = read_input_lines()
    sol1 = part1(memory)
    sol2 = part2(memory)
    copy_sol(sol1, sol2)