from datetime import datetime
import inspect
import os

def read_input(day=None, year=None):
    """Read input file for given day."""
    if day is None:
        day = get_day_num()
    year = year or datetime.now().year
    with open(f'inputs/{year}/day{day:02d}.txt') as f:
        return f.read().strip()

def read_input_lines(day=None):
    """Read input file for given day and return list of lines."""
    if day is None:
        day = get_day_num()
    return read_input(day).split('\n')

def get_day_num():
    # Get the path of the file that called this function
    caller_frame = inspect.stack()[-1]
    caller_path = os.path.dirname(os.path.abspath(caller_frame.filename))
    dir_name = os.path.basename(caller_path)
    return int(dir_name.replace('day', ''))