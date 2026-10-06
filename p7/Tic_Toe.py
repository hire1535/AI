board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def show_board():

    print(board[0], "|", board[1], "|", board[2])
    print("--+---+---")

    print(board[3], "|", board[4], "|", board[5])
    print("--+---+---")

    print(board[6], "|", board[7], "|", board[8])
    print("--+---+---")


def check_winner():

    if board[0] == board[1] == board[2] != " ":
        return True

    if board[3] == board[4] == board[5] != " ":
        return True

    if board[6] == board[7] == board[8] != " ":
        return True

    if board[0] == board[3] == board[6] != " ":
        return True

    if board[1] == board[4] == board[7] != " ":
        return True

    if board[2] == board[5] == board[8] != " ":
        return True

    if board[0] == board[4] == board[8] != " ":
        return True

    if board[2] == board[4] == board[6] != " ":
        return True

    return False


Player = "X"

for turn in range(9):

    show_board()

    position = int(input("Enter the number between 1-9: "))

    if board[position - 1] == " ":

        board[position - 1] = Player

        if check_winner():
            show_board()
            print(Player, "Win")
            break

        if Player == "X":
            Player = "O"
        else:
            Player = "X"

    else:
        print("Already Taken")

else:
    show_board()
    print("Match Draw")