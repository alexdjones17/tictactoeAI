import random
import util

def randomai(board, player):
    return _random_move(board)

def _random_move(board):
    moves = util.get_legal_moves(board)
    return random.choice(moves)