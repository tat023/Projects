# portfolio-project

This project is my portfolio project for Intro to Python II. Contains a class called Othello that allows two people to play text-based Othello (https://en.wikipedia.org/wiki/Reversi).  The Othello game is a strategy board game. In this game, two players take turns placing their colored pieces on an 8x8 board. The objective is to capture the opponent's pieces and have the majority of your own pieces on the board at the end of the game

**Rules:**

* The game is played on an 8x8 board.
* Players take turns placing their pieces on the board, starting with black.
* To capture pieces, a player must place their piece adjacent to an opponent's piece, forming a straight line of adjacent pieces (horizontal, vertical, or diagonal) with their piece at each end.
* Multiple chains/directions of pieces can be captured all at once in a single move, and the captured pieces are converted to the capturing player's color. 
* The game starts with four pieces placed in the middle of the board, forming a square with same-colored pieces on a diagonal.
* Once a piece is placed, it cannot be moved to a new square.
* If a player cannot make a valid move(a capturing move), their turn passes to the other player.
* The game ends when neither player can move, and the player with the most pieces on the board wins. A tie occurs if both players have the same number of pieces.

For a better understanding of the rules, you can play the game at this site: https://www.eothello.com/

**Game Board:**
The game board is represented by a 10x10 grid as figure 1 shown below.
* Edge: * (star)
* Black piece: X
* White piece: O
* Empty space: .  (dot)

Each position on the board could be represented by a (row, column) pair.  For example, at the beginning, white pieces are at position (4,4) and (5,5) and black pieces are at (4,5) and (5,4).

**Player:**
The Player class represents a player in the game. It contains the following information:
* Player name (string)
* Piece color (string): Either "black" or "white"

**Othello:**
The Othello object represents the game as played.  It contains information about the players and the board. 





