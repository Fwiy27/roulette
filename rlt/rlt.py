import random
from board.logic import *

def spin() -> int:
    return random.randint(0, 37)

# Modes: 
    #1 (Color), 
    #2 (Number), 
    #3 (1-12), 
    #4 (13-24), 
    #5 (25-36), 
    #6 (Even), 
    #7 (Odd), 
    #8 (1-18), 
    #9 (19-36)
def check_win(mode, winning_index, bet, number=None, color=None) -> list:
    match mode:
        # 1 - Color
        case 1:
            match color:
                case 'red':
                    return [bet, True] if is_red(winning_index) else [(bet * -1), False]
                case 'black':
                    return [bet, True] if is_black(winning_index) else [(bet * -1), False]
                case 'green':
                    return [(bet * 18), True] if is_green(winning_index) else [(bet * -1), False]
        # 2 - Number
        case 2:
            return [(bet * 35), True] if winning_index == number else [(bet * -1), False]
        # 3 - 1-12
        case 3:
            return [(bet * 2), True] if (1 <= winning_index <= 12) else [(bet * -1), False]
        # 4 - 13-24
        case 4:
            return [(bet * 2), True] if (13 <= winning_index <= 24) else [(bet * -1), False]
        # 5 - 25-36
        case 5:
            return [(bet * 2), True] if (25 <= winning_index <= 36) else [(bet * -1), False]
        # 6 - Even
        case 6:
            return [(bet), True] if winning_index % 2 == 0 and winning_index != 0 else [(bet * -1), False]
        # 7 - Odd
        case 7:
            return [(bet), True] if winning_index % 2 != 0 and winning_index != 37 else [(bet * -1), False]
        # 8 - 1-18 
        case 8:
            return [(bet), True] if (1 <= winning_index <= 18) else [(bet * -1), False]
        #9 - 19-36
        case 9:
            return [(bet), True] if (19 <= winning_index <= 36) else [(bet * -1), False]