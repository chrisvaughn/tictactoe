#!/usr/bin/env python3


class Board:
    def __init__(self):
        self.board = []
        self.rows = 3
        self.columns = 3

        for _ in range(self.rows * self.columns):
            self.board.append(Square())

    def render(self, show_square_num=False):
        for i, s in enumerate(self.board):
            if i != 0 and i % self.columns == 0:
                print()
                print("-----+-----+-----")
            if show_square_num:
                d = f"  {s.display(default=str(i+1))}  "
            else:
                d = f"  {s.display()}  "
            if i % self.columns != 2:
                d += "|"
            print(d, end="")
        print("\n")

    def set(self, square_num, xo):
        i = square_num - 1
        self.board[i].state = xo

    def game_over(self):
        for s in self.board:
            if s.state is None:
                return False
        return True


class Square:
    X = "X"
    O = "O"
    EMPTY = " "

    def __init__(self, state=None):
        self.state = state

    def display(self, default=EMPTY):
        if self.state:
            return self.state
        else:
            return default

    def __str__(self):
        return self.display()

    def __repr__(self):
        return f"<Square state:{self.display()}>"


def valid_mark(player, turn):
    while "the answer is invalid":
        reply = input(f"{player} place a {turn} in square [1-9]: ").lower().strip()
        try:
            move = int(reply)
        except ValueError:
            move = 0
        if 1 <= move <= 9:
            return move


def main():
    print("Welcome to Tic Tac Toe!")
    print("Player 1 will be X, player 2 will be O")
    print()
    b = Board()
    print("Here's the numbering system")
    b.render(show_square_num=True)
    turn = Square.X
    while not b.game_over():
        if turn == Square.X:
            player = "Player 1"
        else:
            player = "Player 2"
        square_num = valid_mark(player, turn)
        b.set(square_num, turn)
        b.render()
        if turn == Square.X:
            turn = Square.O
        else:
            turn = Square.X
    print("Game Over!")


if __name__ == "__main__":
    main()
