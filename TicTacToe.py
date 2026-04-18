board = ["", "", ""
        , "", "", ""
        , "", "", ""]

def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def check_win(player):
    win_positions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
    [0, 4, 8], [2, 4, 6]             # diagonals
    ]

    for pos in win_positions:
        if board[pos [0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

Player = "X"
for turn in range(9):
    print_board()
    move = int(input(f"PLayer {Player}, enter your move (0-8): "))
    if board[move] == "":
        board[move] = Player
    else:
        print(" Position already taken!")
        continue

    if check_win(Player):
        print_board()
        print(f"Player {Player} wins!")
        break

    Player = "O" if Player == "X" else "X"
else:
    print_board()
    print("It's a draw!")