name_list = ['h', 'j', 'k']
pin_list = [1234, 5678, 9000]
balance_list = [1000, 500, 3000]


def withdraw():
    w_amount = int(input("Withdrawal amount: "))
    if w_amount > 0:
        balance_list[i] = balance_list[i] - w_amount
        if balance_list[i] > 0:
            print("Withdrawal successful. New balance:", balance_list[i])
        elif balance_list[i] <= 0:
            print("Balance is insufficient to meet the withdrawal amount.")
    elif w_amount <= 0:
        print("Withdrawal amount can not be negative.")


def deposit():
    d_amount = int(input("Deposit amount: "))
    if d_amount > 0:
        balance_list[i] = balance_list[i] + d_amount
        print("Deposit successful. New balance:", balance_list[i])
    elif d_amount <= 0:
        print("Deposit amount can not be negative.")


def transfer():
    t_user = input("Enter the username you would like to transfer to: ")
    for y in range(len(name_list)):
        if t_user == name_list[y] and balance_list[y]:
            t_amount = int(input("Enter the amount you would like to transfer: "))
            if t_amount > 0:
                balance_list[i] = balance_list[i] - t_amount
                balance_list[y] = balance_list[y] + t_amount
                if balance_list[i] > 0:
                    print("Transfer successful. You sent", t_amount, "[Currency] to", t_user + '.')
                    print("New balance:", balance_list[i])
                elif balance_list[i] <= 0:
                    print("Balance is insufficient to meet the transfer amount.")
            elif t_amount <= 0:
                print("Insufficient amount. Transfer unsuccessful. Returning to user menu.")


# main
print("Bank program.")
while True:
    print("\n== Menu screen ==\n\nWould you like to login or register?")
    menu = int(input("[1]Login, [2]Register: "))
    # Login
    if menu == 1:
        print("\n== Login screen ==\n")
        name = input("Enter username: ")
        password = int(input("Enter password: "))
        for i in range(len(name_list)):
            if name == name_list[i] and password == pin_list[i]:
                print("\nWelcome back,", name_list[i] + "! Current balance:", balance_list[i], "[Currency]")
                while True:
                    user_menu = int(input("[1]Withdraw, [2]Deposit, [3]Transfer, [4]Logout: "))
                    # Withdraw
                    if user_menu == 1:
                        withdraw()
                    # Deposit
                    elif user_menu == 2:
                        deposit()
                    # Transfer
                    elif user_menu == 3:
                        transfer()
                    # Logout
                    elif user_menu == 4:
                        print("You logged out.")
                        break
    # Register
    elif menu == 2:
        print("\n== Register screen ==\n")
        for i in range(len(name_list)) and range(len(pin_list)) and range(len(balance_list)):
            reg_name = input("Enter a username (Only letters): ")
            reg_pass = int(input("Enter a password (Only numbers): "))
            print("To open an account you need to make an initial deposit.")
            reg_deposit = int(input("Enter a deposit amount: "))
            if reg_deposit > 0:
                name_list.insert(1, reg_name)
                pin_list.insert(1, reg_pass)
                balance_list.insert(1, reg_deposit)
                print("Successfully registered. Returning to menu.")
                break
            elif reg_deposit <= 0:
                print("Registration failed due to insufficient deposit amount. Returning to menu.")
                break
