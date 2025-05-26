BOARD_HEIGHT = 3
BOARD_WIDTH = 3

def new_board():
    board = []
    for i in range(0, BOARD_HEIGHT):
        row = []
        for j in range(0, BOARD_WIDTH):
            row.append(None)
        board.append(row)

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

def get_move():
    x = int(input("What is your move's X coordinate? "))
    y = int(input("What is your move's Y coordinate? "))
    return [x, y]

def make_move(player, board, move_coords):
    if not is_valid_move(board, move_coords):
        raise Exception("({0}, {1}) is not a valid move.".format(move_coords[0], move_coords[1]))

    new_board = []
    for i in range(0, BOARD_HEIGHT):
        row = []
        for j in range(0, BOARD_WIDTH):
            row.append(board[i][j])
        new_board.append(row)
    new_board[move_coords[0]][move_coords[1]] = player
    return new_board

def is_valid_move(board, move_coords):
    return board[move_coords[0]][move_coords[1]] == None
