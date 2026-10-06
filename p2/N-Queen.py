def solve(board, row, n):

    if row == n:
        print("solution")
        for r in board:
            print(" ".join(r))
        print()
        return

    for col in range(n):

        safe = True

        for i in range(row):
            if board[i][col] == "Q":
                safe = False

            if abs(i-row) == abs(col-board[i].index("Q")):
                safe = False

        if safe:
            board[row][col] = "Q"
            solve(board, row+1, n)
            board[row][col] = "."

n = int(input("Enter number of queens: "))

board = [["."] * n for i in range(n)]

solve(board, 0, n)