#!/usr/bin/env python3

def yes_or_no(question):
    while "the answer is invalid":
        reply = input(question+' (y/n): ').lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

def welcome():
    print("Let's Play Tic-Tac-Toe!\n")
    going_first = yes_or_no("Are you going first?")
    print(going_first)


if __name__ == '__main__':
    welcome()