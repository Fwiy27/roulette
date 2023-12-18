from utils.utils import *
from colorama import Fore
from board.logic import numbers

def print_board(highlight_index = None, message = None):
    board = '----------------------------------------------------------\n'
    board += '|'
    for i in range(len(numbers)):
        if i == highlight_index:
            color = Fore.YELLOW
        elif i in [0, 37]:
            color = Fore.GREEN
        elif i % 2 == 0:
            color = Fore.LIGHTBLACK_EX
        else:
            color = Fore.RED
        if i % 19 == 0 and i != 0:
            board += '\n|'
        board += color + numbers[i] + f'{Fore.RESET}|'
    if message:
        board += message
    else:
        board += '\n----------------------------------------------------------'
    print(board)