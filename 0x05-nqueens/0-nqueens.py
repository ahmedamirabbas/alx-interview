#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./0-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(col, board, ans, lr, ud, ld, n):
            if col == n:
                ans.append(list(board))
                return
            for row in range(n):
                if lr[row] == 0 and ld[row + col] == 0 and ud[n - 1 + col - row] == 0:
                    board[row][col] = 'Q'
                    lr[row] = 1
                    ld[row + col] = 1
                    ud[n - 1 + col - row] = 1

                    solve(col + 1, board, ans, lr, ud, ld, n)

                    board[row][col] = '.'
                    lr[row] = 0
                    ld[row + col] = 0
                    ud[n - 1 + col - row] = 0

        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        leftrow = [0] * n
        upperDiagonal = [0] * (2 * n - 1)
        lowerDiagonal = [0] * (2 * n - 1)
        solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
        return ans
