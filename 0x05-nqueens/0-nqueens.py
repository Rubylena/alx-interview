#!/usr/bin/python3

import sys


def nqueens(n):
    def is_valid(board, row, col):
        # check the column
        for i in range(row):
            if board[i] == col:
                return False
            # check diagonals
            if abs(board[i] - col) == row - i:
                return False
        return True

    def backtrack(board, row, solutions):
        if row == n:
            # found a solution
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1, solutions)

    board = [-1] * n
    solutions = []
    backtrack(board, 0, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
