def get_legal_moves(board):
    moves = []
    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == None):
                moves.append([j, i])
    return moves