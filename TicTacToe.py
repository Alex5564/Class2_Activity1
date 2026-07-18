import random
import colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def coloured_cell(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
        
    print(' ' + coloured_cell(board[0]) + ' / ' + coloured_cell(board[1]) + ' / ' + coloured_cell(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + coloured_cell(board[3]) + ' / ' + coloured_cell(board[4]) + ' / ' + coloured_cell(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + coloured_cell(board[6]) + ' / ' + coloured_cell(board[7]) + ' / ' + coloured_cell(board[8]))
    print()

def player_choice(board):
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input("Choose your symbol (X or O): ").upper()
    if symbol == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'
    
def player_move(board, symbol):
    move = -1
    while move not in range (1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input(f"Player {symbol}, enter your move (1-9: "))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move. Please try again.")
        except ValueError:
            print("Please enter a value between 1 and 9.")
    board[move - 1] = symbol

    



    

