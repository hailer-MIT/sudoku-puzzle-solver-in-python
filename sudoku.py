def is_valid(board, row, col, num):
    # Check if the number is already present in the same row
    if num in board[row]:
        return False

    # Check if the number is already present in the same column
    for i in range(9):
        if num == board[i][col]:
            return False

    # Check if the number is already present in the same 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if num == board[start_row + i][start_col + j]:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=" ")
        print()

def get_user_input():
    board = []
    print("Enter the Sudoku puzzle (use 0 for empty cells):")
    for _ in range(9):
        row_input = input("Enter 9 numbers for the row, separated by spaces: ")
        row = list(map(int, row_input.split()))
        board.append(row)
    return board


# Main code execution
board = get_user_input()
print("\nSudoku puzzle:")
print_board(board)

if solve_sudoku(board):
    print("\nSolution:")
    print_board(board)
else:
    print("\nNo solution exists for the given puzzle.")