#!/usr/bin/python3
"""
N Queens Problem Solver

This script solves the N Queens puzzle, placing N non-attacking queens
on an N x N chessboard. The program takes a single integer argument N
and prints all possible solutions.
"""

import sys


def print_solutions(solutions):
    """Print the solutions in the required format.

    Args:
        solutions (list): A list of solutions where each solution
                          is represented as a list of [row, col] pairs.
    """
    for solution in solutions:
        print(solution)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The current state of the board.
        row (int): The current row to check.
        col (int): The current column to check.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens_util(board, row, N, solutions):
    """Utilize backtracking to find all solutions for N Queens.

    Args:
        board (list): The current state of the board.
        row (int): The current row to place a queen.
        N (int): The size of the board (N x N).
        solutions (list): A list to store valid solutions.
    """
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row] = -1  # Reset the position


def solve_n_queens(N):
    """Solve the N Queens problem and return all solutions.

    Args:
        N (int): The size of the board (N x N).

    Returns:
        list: A list of solutions where each solution is a list of
              [row, col] pairs.
    """
    board = [-1] * N
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions


def main():
    """Main function to handle input and output for the N Queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
