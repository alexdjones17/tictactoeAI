import ais

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
    for i in range(0, BOARD_HEIGHT):
        line = "{}|".format(i)
        for j in range(0, BOARD_WIDTH):
            temp = " " if board[i][j] == None else board[i][j]
            line += temp + " "
        line = line[:-1]
        line += "|"
        print(line)
    print(" -------")

def switch_player(player):
    return 'O' if player == 'X' else 'X'

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

def is_board_full(board):
    for i in range(0, BOARD_WIDTH):
        for j in range(0, BOARD_WIDTH):
            if board[i][j] == None:
                return False
    return True

def play():
    board = new_board()
    render(board)
    current_player = 'X'

    while True:
        

        current_player = switch_player(current_player)

        # Current way of getting human input
        # while True:
        #     move = get_move()
        #     if not is_valid_move(board, move):
        #         print("Try again")
        #     else:
        #         break

        move = ais.randomai(board, current_player)

        board = make_move(current_player, board, move)

        # Print out the board
        render(board)
        
        winner = get_winner(board)

        if winner != None:
            print("Player {} wins!".format(winner))
            break

        if is_board_full(board):
            print("Draw")
            break

play()