from argparse import ArgumentParser
import pyperclip
from typing import Any, Optional

def copy_sol(sol1: Optional[Any], sol2: Optional[Any]) -> None:
    parser = ArgumentParser()
    parser.add_argument("-p", "--part", choices=["1", "2"], default="2" if sol2 else "1")
    args = parser.parse_args()
    copy_part = args.part
    sol1, sol2 = str(sol1), str(sol2)
    pyperclip.copy(sol1 if copy_part == "1" else sol2)