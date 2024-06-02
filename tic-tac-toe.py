def print_board(board):
    print(f"{board[0]} |{board[1]} |{board[2]}")
    print("--|--|--")
    print(f"{board[3]} |{board[4]} |{board[5]}")
    print("--|--|--")
    print(f"{board[6]} |{board[7]} |{board[8]}")


def move(board, turn, X, O, play):
    if turn == 1:
        board[play - 1] = 'X'
        X[play - 1] = 1
    else:
        board[play - 1] = 'O'
        O[play - 1] = 1


def check_win(X, O, count):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if X[win[0]] + X[win[1]] + X[win[2]] == 3:
            return 1
        elif O[win[0]] + O[win[1]] + O[win[2]] == 3:
            return 0
        elif count == 9:
            return -1


board = [i for i in range(1, 10)]
X = [0, 0, 0, 0, 0, 0, 0, 0, 0]
O = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1
count = 1
while True:
    if turn == 1:
        print("X's turn: ")
    else:
        print("Z's turn: ")
    while True:
        play = int(input("Enter the position: "))
        if board[play-1] != 'X' and board[play-1] != 'O':
            move(board, turn, X, O, play)
            break
        else:
            print("Enter another cell")
    win = check_win(X, O, count)
    print_board(board)
    if win == 1:
        print("X wins")
        break
    elif win == 0:
        print("O wins")
        break
    elif win == -1:
        print("No winner! Game over")
        break
    count = count + 1
    turn = 1 - turn
