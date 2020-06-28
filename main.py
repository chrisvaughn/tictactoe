#!/usr/bin/env python3


class Board:
    def __init__(self):
        self.board = []
        self.rows = 3
        self.columns = 3

        for _ in range(self.rows * self.columns):
            self.board.append(Square())

    def render(self):
        for i, s in enumerate(self.board):
            if i % self.columns == 0:
                print()
            print(s.display() + " ", end="")
        print()

    def set(self, square_num, xo):
        i = square_num - 1
        self.board[i].state = xo


class Square:
    X = "X"
    O = "O"
    EMPTY = "-"

    def __init__(self, state=None):
        self.state = state

    def display(self):
        if self.state:
            return self.state
        else:
            return Square.EMPTY

    def __str__(self):
        return self.display()

    def __repr__(self):
        return f"<Square state:{self.display()}>"


def main():
    b = Board()
    b.render()
    b.set(5, Square.O)
    b.render()
    b.set(7, Square.O)
    b.render()
    b.set(1, Square.X)
    b.render()
    b.set(9, Square.X)
    b.render()
    b.set(2, Square.X)
    b.render()
    b.set(4, Square.X)
    b.render()
    b.set(6, Square.X)
    b.render()
    b.set(8, Square.X)
    b.render()
    b.set(3, Square.O)
    b.render()


if __name__ == "__main__":
    main()
