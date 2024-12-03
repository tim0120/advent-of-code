from datetime import datetime

def read_input(day, year=None):
    """Read input file for given day."""
    year = year or datetime.now().year
    with open(f'inputs/{year}/day{day:02d}.txt') as f:
        return f.read().strip()

def read_input_lines(day):
    """Read input file for given day and return list of lines."""
    return read_input(day).split('\n')
