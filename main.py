#!/usr/bin/env python3


class Board:
    size = 9

    def __init__(self):
        self.board = []

        for _ in range(Board.size):
            self.board.append(Square())

    def render(self):
        for i, s in enumerate(self.board):
            if i % 3 == 0:
                print()
            print(s.display() + " ", end="")
        print()

    def set(self, square_num, xo):
        i = square_num - 1
        self.board[i].state = xo


class Square:
    def __init__(self, state=None):
        self.state = state

    def display(self):
        if self.state:
            return self.state
        else:
            return "-"

    def __str__(self):
        return self.display()

    def __repr__(self):
        return f"<Square state:{self.display()}>"


def main():
    b = Board()
    b.render()
    b.set(5, "o")
    b.render()
    b.set(7, "o")
    b.render()
    b.set(1, "x")
    b.render()
    b.set(9, "x")
    b.render()
    b.set(2, "x")
    b.render()
    b.set(4, "x")
    b.render()
    b.set(6, "x")
    b.render()
    b.set(8, "x")
    b.render()
    b.set(3, "o")
    b.render()


if __name__ == "__main__":
    main()
