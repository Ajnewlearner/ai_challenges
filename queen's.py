N = 8  # board size

def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print("\n")

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, row=0):
    if row == N:
        print_board(board)  # Print solution
        return True  # To stop at first solution, else continue
    
    res = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            res = solve(board, row + 1) or res
            board[row][col] = 0  # backtrack
    
    return res


# Driver code
board = [[0]*N for _ in range(N)]
solve(board)
