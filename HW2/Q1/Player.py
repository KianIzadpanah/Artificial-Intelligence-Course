from Board import BoardUtility
import alpha_beta 
import random
import math


class Player:
    def __init__(self, player_piece):
        self.piece = player_piece

    def play(self, board):
        return 0


class RandomPlayer(Player):
    def play(self, board):
        return random.choice(BoardUtility.get_valid_locations(board))


class HumanPlayer(Player):
    def play(self, board):
        move = int(input("input the next column index 1 to 9:")) - 1
        row = move // 3
        col = move % 3
        return row, col


class MiniMaxPlayer(Player):
    def __init__(self, player_piece, depth=5):
        super().__init__(player_piece)
        self.depth = depth

    def play(self, board):
        value, move = alpha_beta.minimax(board, self.piece, 0, True, -math.inf, math.inf)
        return move


class MiniMaxProbPlayer(Player):
    def __init__(self, player_piece, depth=5, prob_stochastic=0.1):
        super().__init__(player_piece)
        self.depth = depth
        self.prob_stochastic = prob_stochastic

    def play(self, board):
        return alpha_beta.minimax_prob(board, 1 if self.piece == 2 else 2, self.piece, 0, False, -math.inf, math.inf, self.prob_stochastic)

