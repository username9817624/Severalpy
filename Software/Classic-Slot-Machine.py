import random
import os
import time

c_balance = [10000000000000]
c_payout = [0]
s_win = 0
s_loss = 0


def display_func():
    w_con()
    print('\n|¤' + '-' * 11 + '¤|\n||', dp[0][0], '|', dp[0][1], '|', dp[0][2], '||')
    print('|>', dp[1][0], '|', dp[1][1], '|', dp[1][2], '<|\n||', dp[2][0], '|', dp[2][1], '|', dp[2][2], '||')
    print('|¤' + '-' * 11 + '¤|')


def w_payout(v):
    global c_balance
    global c_payout
    global s_win
    global s_loss
    c_payout = u_bet * v - u_bet
    print("\nWin. You have won: $" + str(c_payout))
    c_balance[0] = c_balance[0] - c_payout
    c_payout = c_payout - c_payout
    s_win += 1
    s_loss = s_loss - 1


def w_con():
    print("Win conditions:")
    print(" =, x1000\n B, x50\n S, x2\n O, x1.5\n %, x1.05")


def win_func(x, y):
    global c_balance
    global c_payout
    if x in dp[1][0] and x in dp[1][1] and x in dp[1][2]:
        if x == '=':
            w_payout(1000)
        elif x == 'B':
            w_payout(50)
        elif x == 'S':
            w_payout(2)
        elif x == 'O':
            w_payout(1.5)
        elif x == '%':
            w_payout(1.05)
    elif x in dp[1][0] and x in dp[1][1] and y in dp[1][2]:
        if x == 'B' and y == '=':
            w_payout(50)
        elif x == 'S' and y == '=':
            w_payout(2)
        elif x == 'O' and y == '=':
            w_payout(1.5)


def win_check():
    global s
    win_func(s[0], str(0))
    win_func(s[1], s[0])
    win_func(s[2], s[0])
    win_func(s[3], s[0])
    win_func(s[4], str(0))


# main
while True:
    while True:
        w_con()
        u_bet = int(input("Max bet: $75000 ; Min bet: $1\nEnter your bet amount: $"))
        if 75000 >= u_bet >= 1:
            print("The bet of $" + str(u_bet), "has been registered.")
            time.sleep(1)
            os.system('cls||clear')
            break
        elif u_bet <= 0:
            print("Bet can not be negative.")
            time.sleep(1)
            os.system('cls||clear')
            continue
    while True:
        s_loss = s_loss + 1
        s = ['=', 'B', 'S', 'O', '%']
        p = ['=', 'B', 'S', 'O', '%', '-']
        dp = [[random.choice(s), random.choice(s), random.choice(s)],
              [random.choice(p), random.choice(p), random.choice(p)],
              [random.choice(s), random.choice(s), random.choice(s)]]
        display_func()
        win_check()
        print("\nBet amount: $" + str(u_bet))
        print("Stats: Wins -", s_win, "Losses -", s_loss)
        user_input = input("\nChange bet: Hit 's' + 'enter'\nBet again: Hit 'enter'\n> ")
        if user_input == '':
            c_balance[0] = c_balance[0] + u_bet
            os.system('cls||clear')
            continue
        elif user_input == 's':
            os.system('cls||clear')
            break
        else:
            exit()
