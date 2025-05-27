BOARD_HEIGHT = 3
BOARD_WIDTH = 3

def new_board():
    board = []
    for i in range(0, BOARD_WIDTH):
        row = []
        for j in range(0, BOARD_HEIGHT):
            row.append(None)
        board.append(row)

    return board

def render(board):
    print("  0 1 2")
    print(" -------")
    for i in range(0, BOARD_WIDTH):
        line = "{}|".format(i)
        for j in range(0, BOARD_HEIGHT):
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
    for i in range(0, BOARD_WIDTH):
        row = []
        for j in range(0, BOARD_HEIGHT):
            row.append(board[i][j])
        new_board.append(row)
    new_board[move_coords[1]][move_coords[0]] = player
    return new_board

def is_valid_move(board, move_coords):
    return board[move_coords[1]][move_coords[0]] == None

def get_winner(board):
    lines = []

    for i in range(0, BOARD_WIDTH):
        lines.append(board[i])

    for i in range(0, BOARD_HEIGHT):
        temp = []
        for j in range(0, BOARD_WIDTH):
            temp.append(board[j][i])
        lines.append(temp)

    temp = []
    for i in range(0, BOARD_WIDTH):
        temp.append(board[i][i])
    lines.append(temp)

    temp = []
    temp.append(board[2][0])
    temp.append(board[1][1])
    temp.append(board[0][2])
    lines.append(temp)

    for i in range(0, len(lines)):
        if lines[i][0] == lines[i][1] and lines[i][1] == lines[i][2]:
            return lines[i][0]
    return None

def check_draw(board):
    for i in range(0, BOARD_WIDTH):
        for j in range(0, BOARD_WIDTH):
            if board[i][j] == None:
                return False
    return True

board = new_board()
player = 'X'

while True:
    # Print out the board
    render(board)

    player = 'O' if player == 'X' else 'X'

    while True:
        move = get_move()
        if not is_valid_move(board, move):
            print("Try again")
        else:
            break

    board = make_move(player, board, move)
    
    winner = get_winner(board)

    if winner != None:
        print("Player {} wins!".format(winner))
        break

    if check_draw(board):
        print("Draw")
        break
