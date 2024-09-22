import numpy as np


class BoardUtility:

    @staticmethod
    def has_player_won(game_board, player_piece):
        """
        piece:  1 or 2.
        return: True if the player with the input piece has won.
                False if the player with the input piece has not won.
        """
        # checking horizontally
        for r in range(3):
            if game_board[r][0] == player_piece and game_board[r][1] == player_piece and game_board[r][
                2] == player_piece:
                return True

        # checking vertically
        for c in range(3):
            if game_board[0][c] == player_piece and game_board[1][c] == player_piece and game_board[2][
                c] == player_piece:
                return True

        # checking diagonally
        if game_board[0][0] == player_piece and game_board[1][1] == player_piece and game_board[2][
            2] == player_piece:
            return True

        if game_board[0][2] == player_piece and game_board[1][1] == player_piece and game_board[2][
            0] == player_piece:
            return True

        return False

    @staticmethod
    def is_draw(game_board):
        return not np.any(game_board == 0)

    @staticmethod
    def point_calculator(num_player1, num_player2):
        sum = 0
        if num_player1 == 3:
            sum += 100
        elif num_player1 == 2:
            sum += 10
        elif num_player1 == 1:
            sum += 1
        if num_player2 == 3:
            sum -= 100
        elif num_player2 == 2:
            sum -= 10
        elif num_player2 == 1:
            sum -= 1
        return sum
    @staticmethod
    def opponent(piece):
        if piece == 1:
            return 2
        return 1

    @staticmethod
    def score_position(game_board, piece):
        if BoardUtility.has_player_won(game_board, piece):
            return 100
        if BoardUtility.has_player_won(game_board, 1 if piece == 2 else 2):
            return -100
        tot_sum = 0
        # check horizontally
        for j in range(3):
            num_player1 = 0
            num_player2 = 0
            for i in range(3):
                if game_board[i][j] == piece:
                    num_player1 += 1
                elif game_board[i][j] == 0:
                    a = 0
                else:
                    num_player2 += 1
            tot_sum += BoardUtility.point_calculator(num_player1, num_player2)

        # check vertically
        for j in range(3):
            num_player1 = 0
            num_player2 = 0
            for i in range(3):
                if game_board[j][i] == piece:
                    num_player1 += 1
                elif game_board[j][i] == 0:
                    a = 0
                else:
                    num_player2 += 1
            tot_sum += BoardUtility.point_calculator(num_player1, num_player2)

        # check diagonally
        num_player1 = 0
        num_player2 = 0
        for i in range(3):
            if game_board[i][i] == piece:
                num_player1 += 1
            elif game_board[i][i] == 0:
                a = 0
            else:
                num_player2 += 1
        tot_sum += BoardUtility.point_calculator(num_player1, num_player2)
        num_player1 = 0
        num_player2 = 0
        for i in range(3):
            if game_board[i][2 - i] == piece:
                num_player1 += 1
            elif game_board[i][2 - i] == 0:
                a = 0
            else:
                num_player2 += 1
        tot_sum += BoardUtility.point_calculator(num_player1, num_player2)

        return tot_sum


    @staticmethod
    def get_valid_locations(game_board):
        """
        returns all the valid locations to make a move.
        """
        valid_locations = []

        for i in range(3):
            for j in range(3):
                if game_board[i, j] == 0:
                    valid_locations.append((i, j))
        return valid_locations

    @staticmethod
    def is_terminal_state(game_board):
        """
        return True if either of the player have won the game or we have a draw.
        """
        return BoardUtility.has_player_won(game_board, 1) or \
               BoardUtility.has_player_won(game_board, 2) or BoardUtility.is_draw(game_board)

    @staticmethod
    def make_move(game_board, row, col, player):
        """
        make a new move on the board
        row & col: row and column of the new move
        piece: 1 for first player. 2 for second player
        """
        assert game_board[row][col] == 0
        game_board[row][col] = player
