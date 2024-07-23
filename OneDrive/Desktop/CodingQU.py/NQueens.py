def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check the column for another queen
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check the upper left diagonal for another queen
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check the upper right diagonal for another queen
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        # Check the lower left diagonal for another queen
        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1

        # Check the lower right diagonal for another queen
        i, j = row, col
        while i < n and j < n:
            if board[i][j] == 'Q':
                return False
            i += 1
            j += 1

        return True

    def solve(board, row, results):
        if row == n:
            results.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(board, row + 1, results)
                board[row][col] = '.'
    
    board = [['.' for _ in range(n)] for _ in range(n)]
    results = []
    solve(board, 0, results)
    return results

# Example usage:
n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
for solution in solutions:
    for row in solution:
        print(row)
    print()
  