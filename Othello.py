# Author: Terrie Tran
# GitHub: tat023
# Date: 5/28/23
# Description: A two player text-based Othello game with two classes: Player and Othello.


class Othello:
    """Represents the game object and the board. Works with the Player class to track a player list, determine
    the winning player, and update the board using the piece color and position passed in the main function"""

    def __init__(self):
        self._board = [["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
                       ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
                       ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
                       ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
                       ["*", ".", ".", ".", "0", "X", ".", ".", ".", "*"],
                       ["*", ".", ".", ".", "X", "0", ".", ".", ".", "*"],
                       ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
                       ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
                       ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
                       ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
                       ]
        self._player_list = []
        self._avail_moves = []
        self._player_position0 = []
        self._player_positionX = []
        self._black_count = 0
        self._white_count = 0

    def print_board(self):
        """Returns the board (self._board) with a print statement, including the boundaries"""
        for row in self._board:
            for item in row:
                print(item, end=" ")
            print()

    def create_player(self, player_name, color):
        """Returns a player object using the parameters: player name (string) and color ("black" or "white")
        and adds it to the player list"""
        player_object = Player(player_name, color)
        self._player_list.append(player_object)
        return player_object

    def get_list(self):
        """Takes no parameters and returns the list of players"""
        return self._player_list

    def get_positions(self):
        """Takes no parameters and returns two lists of the spaces each player occupies"""
        return f"These are the black pieces positions: {self._player_positionX}\nThese are the " \
               f"white pieces positions" \
               f"{self._player_position0}"

    def return_winner(self):
        """Takes no parameters and returns "Winner is white player: player’s name" if white player wins,
        returns "Winner is black player: player’s name" if black player wins,
        and returns "It's a tie" if black and white player has the same number of pieces
        when the game ends."""
        for rows in range(len(self._board)):
            for elements in self._board[rows]:
                if "X" in elements:
                    self._black_count += 1
                if "0" in elements:
                    self._white_count += 1
        for player in self._player_list:
            if self._black_count > self._white_count:
                if "black" in player.get_color():
                    print(f"Winner is black player:", player.get_player())
            if self._white_count > self._black_count:
                if "white" in player.get_color():
                    print(f"Winner is white player:", player.get_player())
        if self._black_count == self._white_count:
            print("It's a tie")

    def return_available_positions(self, color):
        """Returns a list of possible positions for the player with the parameter color to move on the current board."""
        self._player_position0 = []
        self._player_positionX = []
        self._avail_moves = set()
        move_direction = [-1, 0, 1]
        piece_move = False
        for row in range(len(self._board)):
            nested_lists = self._board[row]
            for column in range(len(nested_lists)):
                if nested_lists[column] == "X":
                    self._player_positionX.append((row, column))  # keeps track of all spaces occupied by both players
                    if color == "black":
                        for direction in move_direction:
                            new_coords1 = [(row + direction, column) for row, column in self._player_position0]
                            new_coords2 = [(row, column + direction) for row, column in self._player_position0]
                            for coords in new_coords1:
                                piece_move = self.valid_move(color, coords)
                            if piece_move is True:
                                self._avail_moves.add(coords)
                            for coords in new_coords2:
                                piece_move = self.valid_move(color, coords)
                            if piece_move is True:
                                self._avail_moves.add(coords)
                if nested_lists[column] == "0":
                    self._player_position0.append((row, column))
                if color == "white":
                    for direction in move_direction:
                        new_coords1 = [(row + direction, column) for row, column in self._player_positionX]
                        new_coords2 = [(row, column + direction) for row, column in self._player_positionX]
                    for coords in new_coords1:
                        piece_move = self.valid_move(color, coords)
                    if piece_move is True:
                        self._avail_moves.add(coords)
                    for coords in new_coords2:
                        piece_move = self.valid_move(color, coords)
                    if piece_move is True:
                        self._avail_moves.add(coords)
        return sorted(self._avail_moves)

    def valid_move(self, color, piece_position):  # issue is another piece needs to be diagonal, horizontal, vertical
        """Helper method to return_available_positions, checks the available positions is valid. Takes as a parameter
         the color and piece position and returns if the moves valid without changing the board"""
        num_list = []
        valid_move = False
        for num in piece_position:
            num_list.append(num)
        row_val = num_list[0]
        column_val = num_list[1]
        next_to = [-1, 0, 1]
        diagonal_move = 0
        for direction in next_to:  # direction is -1 or 1
            row_direction = row_val + direction  # row -1 (up) or +1 (down) 4
            column_direction = column_val + direction  # column -1 (left) or +1 (right) 5
            if self._board[row_val][column_val] == "." and color == "black":  # valid move only if the space is empty
                # checking player color
                if "0" in self._board[row_direction][column_val] or "0" in self._board[row_val][column_direction]:
                    if "X" in self._board[row_val] or "X" in self._board[column_direction]:
                        valid_move = True
                        if "0" in self._board[row_val] or "0" in self._board[column_direction]:
                            for num in range(len(self._board[row_val])):
                                if "0" in self._board[row_val][num]:
                                    valid_move = True
                                if "0" in self._board[num][column_val]:
                                    valid_move = True
                while (diagonal_move + row_val < 9 and diagonal_move + column_val < 9) \
                        or (row_val - diagonal_move > 0 and column_val - diagonal_move < 0):
                    diagonal_move += 1
                    neg_tracker1 = row_val - diagonal_move
                    neg_tracker2 = column_val - diagonal_move
                    pos_tracker1 = diagonal_move + row_val
                    pos_tracker2 = diagonal_move + column_val
                    if "X" in self._board[neg_tracker1][neg_tracker2] \
                            or "X" in self._board[pos_tracker1][pos_tracker2] \
                            and self._board[row_val][column_val] != "*":
                        valid_move = True
                    if self._board[neg_tracker1][neg_tracker2] == "0":
                        valid_move = True
                    if self._board[pos_tracker1][pos_tracker2] == "0":
                        valid_move = True
            if self._board[row_val][column_val] == "." and color == "white":
                if "X" in self._board[row_direction][column_val] or "X" in self._board[row_val][column_direction]:
                    if "0" in self._board[row_val] or "0" in self._board[column_direction]:
                        if "X" in self._board[row_val] or "X" in self._board[column_direction]:
                            for num in range(len(self._board[row_val])):
                                if "X" in self._board[row_val][num]:
                                    valid_move = True
                                if "X" in self._board[num][column_val]:
                                    valid_move = True
                    elif "X" not in self._board[row_direction][column_val] or "X" not in self._board[row_val][
                        column_direction]:
                        valid_move = False
                    while (diagonal_move + row_val < 9 and diagonal_move + column_val < 9) \
                            or (row_val - diagonal_move > 0 and column_val - diagonal_move < 0):
                        diagonal_move += 1
                        neg_tracker1 = row_val - diagonal_move
                        neg_tracker2 = column_val - diagonal_move
                        pos_tracker1 = diagonal_move + row_val
                        pos_tracker2 = diagonal_move + column_val
                        if "0" in self._board[neg_tracker1][neg_tracker2] \
                                or "0" in self._board[pos_tracker1][pos_tracker2] \
                                and self._board[row_val][column_val] != "*":
                            valid_move = True
                        if self._board[neg_tracker1][neg_tracker2] == "X":
                            valid_move = True
                        if self._board[pos_tracker1][pos_tracker2] == "X":
                            valid_move = True
        return valid_move

    def make_move(self, color, piece_position):
        """Takes color and piece_position as a parameters and puts the corresponding piece at the
        given position and updates the board accordingly,
        then returns the current board as a 2d list."""
        # i need several things: the same piece needs to be in that row, column, or diagonal which is 1x1 times whatever
        # spaces away
        # a valid move is placed next to the opposite piece and is horizontal, diagonal, or vertical, and is not taken
        # captures all the pieces in between
        num_list = []
        for num in piece_position:
            num_list.append(num)
        row_val = num_list[0]
        column_val = num_list[1]
        next_to = [-1, 0, 1]
        diagonal_move = 0
        for direction in next_to:  # direction is -1 or 1
            row_direction = row_val + direction  # row -1 (up) or +1 (down) 4
            column_direction = column_val + direction  # column -1 (left) or +1 (right) 5
            if self._board[row_val][column_val] == "." and color == "black":  # valid move only if the space is empty
                # checking player color
                if "0" in self._board[row_direction][column_val] or "0" in self._board[row_val][column_direction]:
                    if "X" in self._board[row_val] or "X" in self._board[column_direction]:
                        self._board[row_val][column_val] = "X"
                        if "0" in self._board[row_val] or "0" in self._board[column_direction]:
                            for num in range(len(self._board[row_val])):
                                if "0" in self._board[row_val][num] or "0" in self._board[num][column_val]:
                                    self._board[row_val][num] = "X"
                                if "0" in self._board[num][column_val]:
                                    self._board[num][column_val] = "X"
                while (diagonal_move + row_val < 9 and diagonal_move + column_val < 9) \
                        or (row_val - diagonal_move > 0 and column_val - diagonal_move < 0):
                    diagonal_move += 1
                    neg_tracker1 = row_val - diagonal_move
                    neg_tracker2 = column_val - diagonal_move
                    pos_tracker1 = diagonal_move + row_val
                    pos_tracker2 = diagonal_move + column_val
                    if "X" in self._board[neg_tracker1][neg_tracker2] \
                            or "X" in self._board[pos_tracker1][pos_tracker2] \
                            and self._board[row_val][column_val] != "*":
                        self._board[row_val][column_val] = "X"
                    if self._board[neg_tracker1][neg_tracker2] == "0":
                        self._board[neg_tracker1][neg_tracker2] = "X"
                    if self._board[pos_tracker1][pos_tracker2] == "0":
                        self._board[pos_tracker1][pos_tracker2] = "X"
            if self._board[row_val][column_val] == "." and color == "white":
                if "X" in self._board[row_direction][column_val] or "X" in self._board[row_val][column_direction]:
                    if "0" in self._board[row_val] or "0" in self._board[column_direction]:
                        self._board[row_val][column_val] = "0"
                        if "X" in self._board[row_val] or "X" in self._board[column_direction]:
                            for num in range(len(self._board[row_val])):
                                if "X" in self._board[row_val][num] or "X" in self._board[num][column_val]:
                                    self._board[row_val][num] = "0"
                    while (diagonal_move + row_val < 9 and diagonal_move + column_val < 9) \
                            or (row_val - diagonal_move > 0 and column_val - diagonal_move < 0):
                        diagonal_move += 1
                        neg_tracker1 = row_val - diagonal_move
                        neg_tracker2 = column_val - diagonal_move
                        pos_tracker1 = diagonal_move + row_val
                        pos_tracker2 = diagonal_move + column_val
                        if "0" in self._board[neg_tracker1][neg_tracker2] \
                                or "0" in self._board[pos_tracker1][pos_tracker2] \
                                and self._board[row_val][column_val] != "*":
                            self._board[row_val][column_val] = "0"
                        if self._board[neg_tracker1][neg_tracker2] == "X":
                            self._board[neg_tracker1][neg_tracker2] = "0"
                        if self._board[pos_tracker1][pos_tracker2] == "X":
                            self._board[pos_tracker1][pos_tracker2] = "0"
        return self._board

    def play_game(self, player_color, piece_position):
        """Takes the player_Color and piece_position as parameters and returns a printed statement that is dependent on
        if a move is valid, invalid, or a winning move.
        Makes a move for the player with based on the player_Color and piece_position parameters.
        If the position is invalid, the function returns "Invalid move" and prints
        "Here are the valid moves:" with the possible moves available.
        If no valid moves exist then the returned list is empty.
        If the position is valid, the function should make that move and update the board.
        If the game is ended at that point, the function should print
        "Game is ended white piece: number black piece: number" and call the return_winner method."""
        piece_move = self.valid_move(player_color, piece_position)
        if piece_move is False:
            return "Invalid Move", print(
                f"Here are the valid moves for {player_color}: {self.return_available_positions(player_color)}")
        if piece_move == self._board[0] or piece_move == self._board[9]:
            return "Invalid Move", print(
                f"Here are the valid moves: {self.return_available_positions(player_color)}")
        if piece_move is False and self.make_move(player_color, piece_position) is False:
            print(f"Game is ended white piece: {self._white_count} black piece: {self._black_count}")
            return self.return_winner()
        else:
            self.make_move(player_color, piece_position)


class Player:
    """Represents a player in the game. The attributes are player name (string) and
    the piece color (black or white string). Works with the Othello class to update the board and keep track of the
    players and player positions"""

    def __init__(self, player_name, piece_color):
        self._player_name = player_name
        valid_colors = ["white", "black"]
        if piece_color not in valid_colors:
            raise ColorError(f"{piece_color} is not a valid color")
        else:
            self._piece_color = piece_color

    def get_player(self):
        """Returns the player name"""
        return self._player_name

    def set_player(self, player_name):
        """Sets the player name attribute"""
        self._player_name = player_name

    def get_color(self):
        """Returns the piece color"""
        return self._piece_color

    def set_color(self, piece_color):
        """Sets the piece color"""
        self._piece_color = piece_color


class ColorError(Exception):
    """user-defined exception for invalid color input"""
    pass


def main():
    game = Othello()
    game.create_player("Helen", "white")
    game.create_player("Leo", "black")
    game.print_board()
    game.make_move("black", (5, 6))
    game.print_board()
    game.play_game("white", (6, 4))
    print("Valid moves: (4,6), (6,4), (6,6)")
    game.return_winner()
    game.print_board()
    game.print_board()
    print("Next Game")
    game1 = Othello()
    game1.print_board()
    game1.create_player("Helen", "white")
    game1.create_player("Leo", "black")
    game1.play_game("black", (6, 5))
    game1.print_board()
    game1.play_game("white", (6, 6))
    game1.print_board()
    game1.return_winner()


if __name__ == '__main__':
    main()
