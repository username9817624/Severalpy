board = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]


def board_user(Y):
    if 0 <= user_num <= 9:
        if user_num == 1 and board[0][0] == '#':
            board[0][0] = Y
        elif user_num == 2 and board[0][1] == '#':
            board[0][1] = Y
        elif user_num == 3 and board[0][2] == '#':
            board[0][2] = Y
        elif user_num == 4 and board[1][0] == '#':
            board[1][0] = Y
        elif user_num == 5 and board[1][1] == '#':
            board[1][1] = Y
        elif user_num == 6 and board[1][2] == '#':
            board[1][2] = Y
        elif user_num == 7 and board[2][0] == '#':
            board[2][0] = Y
        elif user_num == 8 and board[2][1] == '#':
            board[2][1] = Y
        elif user_num == 9 and board[2][2] == '#':
            board[2][2] = Y


def board_check_win_tie(Q):
    b = [Q, Q, Q]
    if b == board[0] or b == board[1] or b == board[2] or \
            Q in board[0][0] and Q in board[1][0] and Q in board[2][0] or \
            Q in board[0][1] and Q in board[1][1] and Q in board[2][1] or \
            Q in board[0][2] and Q in board[1][2] and Q in board[2][2] or \
            Q in board[0][0] and Q in board[1][1] and Q in board[2][2] or \
            Q in board[0][2] and Q in board[1][1] and Q in board[2][0]:
        print(Q, "is the winner!")
        restart_f()
    elif '#' not in board[0] and '#' not in board[1] and '#' not in board[2]:
        print("Tie.")
        restart_f()


def restart_f():
    global board
    board = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
    restart = input("\nRESTART? (y/n): ")
    if restart == 'y':
        return
    elif restart == 'n':
        exit()


print("== 3x3 Tic Tac Toe ==")
while True:
    print('\n', board[0][0], '|', board[0][1], '|', board[0][2], '\n', '---------', '\n',
          board[1][0], '|', board[1][1], '|', board[1][2], '\n', '---------', '\n',
          board[2][0], '|', board[2][1], '|', board[2][2])
    board_check_win_tie('X')
    board_check_win_tie('O')
    while True:
        user_turn = int(input("\nUser 1 or User 2? (1/2): "))
        user_num = int(input("Enter a number (1-9): "))
        if user_turn == 1:
            board_user('X')
            break
        elif user_turn == 2:
            board_user('O')
            break
