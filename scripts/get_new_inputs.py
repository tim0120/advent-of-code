import os
import time
import requests
from datetime import datetime, date
from pathlib import Path

def get_new_inputs(session_token, year=None):
    """Download all available Advent of Code inputs for specified year."""
    year = year or datetime.now().year
    current_date = date.today()
    
    input_dir = Path('inputs')
    input_dir.mkdir(exist_ok=True)
    
    # Only download up to current day in December
    max_day = 25
    if year == current_date.year and current_date.month == 12:
        max_day = current_date.day
    
    for day in range(1, max_day + 1):
        input_file = input_dir / year / f'day{day:02d}.txt'
        
        if input_file.exists():
            print(f'Skipping day {day}, input already exists')
            continue
        
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        headers = {'Cookie': f'session={session_token}'}
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            input_file.write_text(response.text.rstrip('\n'))
            print(f'Downloaded day {day}')
            
            # Be nice to the server
            time.sleep(1)
            
        except requests.RequestException as e:
            print(f'Error downloading day {day}: {e}')

if __name__ == '__main__':
    session_token = os.getenv('AOC_SESSION')
    if not session_token:
        print('Please set AOC_SESSION environment variable')
        exit(1)
    
    get_new_inputs(session_token)