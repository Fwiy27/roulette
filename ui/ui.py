from utils.utils import *
from board.board import print_board
from rlt.rlt import check_win, spin
from colorama import Fore

def get_mode(mode) -> str:
    match mode:
        case 1:
            return 'Color (Pays Even Money)'
        case 2:
            return 'Number (Pays 35 to 1)' 
        case 3:
            return '1st 12 (Pays 2 to 1)'
        case 4:
            return '2nd 12 (Pays 2 to 1)'
        case 5:
            return '3rd 12 (Pays 2 to 1)'
        case 6:
            return 'Evens (Pays Even Money)'
        case 7:
            return 'Odds (Pays Even Money)'
        case 8:
            return '1 to 18 (Pays Even Money)'
        case 9:
            return '19 to 36 (Pays Even Money)'



help = '''
MODES = 1 (Color), 2 (Number), 3 (1st 12), 4 (2nd 12), 
    5 (3rd 12), 6 (Even), 7 (Odd), 8 (1-18), 9 (19-36)
Commands: 
set {bet_amount} | Sets bet amount
mode {mode_number} | Sets mode
bet {color/number/None} | Bet, color and number are only for modes 1 and 2
Press Enter to Continue . . .'''

class UI:
    def __init__(self, money=1500, table_min=5, table_max=500):
        # Table Min and Max
        self.table_min = table_min
        self.table_max = table_max
        # Money
        self.starting_money = money
        self.money = money
        self.bet_amount = max(min(round(money * 0.00333333333), table_max), table_min)
        
    def play(self):
        bets = 0
        mode = 1
        ready = False
        while self.money >= self.table_min:
            clear_screen()
            print_board()
            print(f'{Fore.LIGHTBLUE_EX}Mode: {get_mode(mode)}')
            print(f'{Fore.GREEN}Money: {self.money}')
            print(f'{Fore.RED}Bet Amount: {self.bet_amount}{Fore.RESET}')
            check = input('Command: ').split(' ')
            if check[0] == '' and ready:
                pass
            elif check[0] == '':
                pass
            else:
                command = check
                match command[0]:
                    case 'clear':
                        clear_screen()
                        exit()
                    case 'info':
                        clear_screen()
                        ready = False
                        print(f'Money: ${self.money}')
                        print(f'Money Earned: ${(self.money - self.starting_money)}')
                        input(f'Bets: {bets}\nAbout {bets*2/60} hours\nPress Enter to Continue . . .')
                    case 'set':
                        ready = False
                        try:
                            amount = int(command[1])
                            if amount == 0:
                                self.bet_amount = 0
                            else:
                                self.bet_amount = max(min(int(command[1]), self.table_max), self.table_min)
                        except:
                            pass
                    case 'mode':
                        ready = False
                        try:
                            if 1 <= int(command[1]) <= 9:
                                mode = int(command[1])
                        except:
                            pass
                    case 'bet':
                        match mode:
                            case 1:
                                if len(command) == 2 and command[1] in ['red', 'green', 'black']:
                                    ready = True
                                else:
                                    ready = False
                            case 2:
                                try:
                                    if len(command) == 2 and (0<=int(command[1])<=37):
                                        ready = True
                                    else:
                                        ready = False
                                except:
                                    pass
                            case _:
                                if len(command) == 1:
                                    ready = True
                                elif len(command) == 2:
                                    try:
                                        if int(command[1]) == 0:
                                            self.bet_amount = 0
                                        else:
                                            self.bet_amount = min(max(min(int(command[1]), self.table_max), self.table_min), self.money)
                                        ready = True
                                    except:
                                        ready = False
                                else:
                                    ready = False
                    case 'help':
                        clear_screen()
                        input(help)
            if ready:
                bets += 1
                clear_screen()
                winning_index = spin()
                match mode:
                    case 1:
                        win = check_win(mode, winning_index, self.bet_amount, color=command[1])
                    case 2:
                        win = check_win(mode, winning_index,self.bet_amount, number=int(command[1]))
                    case _:
                        win = check_win(mode, winning_index, self.bet_amount)
                self.money += win[0]
                print_board(winning_index)
                if win[1]:
                    print(f'{Fore.GREEN}Money: {self.money}\nWON!')
                else:
                    if self.bet_amount > self.money:
                        self.bet_amount = max(min(round(self.money * 0.00333333333), self.table_max), self.table_min)
                    print(f'{Fore.RED}Money: {self.money}\nLOSE!')
                input(f'Press Enter to Continue . . .{Fore.RESET}')