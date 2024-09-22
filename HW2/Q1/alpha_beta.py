import math
import Board
import random

best_move = (-1, -1)


def minimax(board, player_piece, depth, is_maximizing_player, alpha, beta):
    global best_move
    best_value = -math.inf if is_maximizing_player else math.inf
    if Board.BoardUtility.is_terminal_state(board) or depth == 4:
        return Board.BoardUtility.score_position(board, player_piece), best_move
    child_nodes = Board.BoardUtility.get_valid_locations(board)
    for node in child_nodes:
        board[node[0]][node[1]] = player_piece
        if is_maximizing_player:
            value = minimax(board, player_piece, depth + 1, False, alpha, beta)[0]
            if value > best_value:
                best_value = value
                best_move = node
            alpha = max(alpha, best_value)
            board[node[0]][node[1]] = 0
            if beta <= alpha:
                break

        else:
            value = minimax(board, 1 if player_piece == 2 else 2, depth + 1, True, alpha, beta)[0]
            if value < best_value:
                best_value = value
                best_move = node
            beta = min(beta, best_value)
            board[node[0]][node[1]] = 0
            if beta <= alpha:
                break
        board[node[0]][node[1]] = 0

    return best_value, best_move


def minimax_prob(board, our_piece, enemy_piece, depth, is_maximizing_player, alpha, beta, prob):
    rand = random.random()
    if rand <= prob:
         valid_loc = Board.BoardUtility.get_valid_locations(board)
         rand_index = random.randint(0, len(valid_loc) - 1)
         return valid_loc[rand_index]
    else:
        return minimax(board, enemy_piece, depth, is_maximizing_player, alpha, beta)[1]
         

    
