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


def board_check_win(Q):
    if Q == board[0][0] and Q == board[0][1] and Q == board[0][2] or \
            Q == board[1][0] and Q == board[1][1] and Q == board[1][2] or \
            Q == board[2][0] and Q == board[2][1] and Q == board[2][2] or \
            Q == board[0][0] and Q == board[1][0] and Q == board[2][0] or \
            Q == board[0][1] and Q == board[1][1] and Q == board[2][1] or \
            Q == board[0][2] and Q == board[1][2] and Q == board[2][2] or \
            Q == board[0][0] and Q == board[1][1] and Q == board[2][2] or \
            Q == board[0][2] and Q == board[1][1] and Q == board[2][0]:
        print(Q, "is the winner!")
        restart_f()


def board_check_tie():
    if '#' != board[0][0] and '#' != board[0][1] and '#' != board[0][2] and \
            '#' != board[1][0] and '#' != board[1][1] and '#' != board[1][2] and \
            '#' != board[2][0] and '#' != board[2][1] and '#' != board[2][2]:
        print("Tie.")
        restart_f()


def restart_f():
    board[0][0] = '#'
    board[0][1] = '#'
    board[0][2] = '#'
    board[1][0] = '#'
    board[1][1] = '#'
    board[1][2] = '#'
    board[2][0] = '#'
    board[2][1] = '#'
    board[2][2] = '#'
    restart = input("RESTART? (y/n): ")
    if restart == 'y':
        return
    elif restart == 'n':
        exit()


print("== 3x3 Tic Tac Toe ==")
while True:
    print('\n', board[0][0], '|', board[0][1], '|', board[0][2], '\n', '---------', '\n',
          board[1][0], '|', board[1][1], '|', board[1][2], '\n', '---------', '\n',
          board[2][0], '|', board[2][1], '|', board[2][2])
    board_check_win('X')
    board_check_win('O')
    board_check_tie()
    while True:
        user_turn = int(input("\nUser 1 or User 2? (1/2): "))
        user_num = int(input("Enter a number (1-9): "))
        if user_turn == 1:
            board_user('X')
            break
        elif user_turn == 2:
            board_user('O')
            break
