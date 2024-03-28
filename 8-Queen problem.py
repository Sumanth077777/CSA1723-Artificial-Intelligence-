def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False
    return True
def solve_queens(board, row):
    if row >= len(board):
        return True
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
            board[row] = -1
    return False
def print_board(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
def solve_n_queens(n):
    board = [-1] * n
    if solve_queens(board, 0):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists.")
if __name__ == "__main__":
    solve_n_queens(8)
