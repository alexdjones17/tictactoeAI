BOARD_HEIGHT = 3
BOARD_WIDTH = 3

def new_board():
    board = []
    for i in range(0, BOARD_HEIGHT):
        column = []
        for j in range(0, BOARD_WIDTH):
            column.append(None)
        board.append(column)

    return board

def render(board):
    print("  0 1 2")
    print(" -------")
    for i in range(0, BOARD_HEIGHT):
        line = "{}|".format(i)
        for j in range(0, BOARD_WIDTH):
            temp = " " if board[i][j] == None else board[i][j]
            line += temp + " "
        line = line[:-1]
        line += "|"
        print(line)
    print(" -------")

# Test code
board = new_board()
board[0][0] = 'X'
board[0][1] = 'O'
board[0][2] = 'X'
board[1][1] = 'O'
render(board)

# # Go through turns until the game is over

# while True:
#     # Define the current player
#     current_player = ?

#     # Print the board
#     create(board)

#     # Get the move
#     move = get_move()

#     # Make the move
#     make_move(board, move)

#     # Detect a win
#     winner = detect_winner(board)

#     if winner is something:
#         print("The winner is " + winner)
#         break

#     if is_board_full(board):
#         print("It's a draw!")
#         break

#     # Loops until the game is over