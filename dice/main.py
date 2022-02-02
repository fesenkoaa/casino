import random
import sys


def need_help():
    print("\nCommand list:")
    print("b - bet")
    print("c - credit")
    print("t - throw\n")
    print("h - help")
    print("x - exit\n")


need_help()

credit = 0
bank = 0
bet = 0

while True:

    print(f'Your money: {credit}$')
    print(f'Bet is {bet}$')
    command = input("Input command: ")

    if command == "exit":
        sys.exit()
    elif command == "help":
        need_help()
    elif command == "credit":
        credit = input("Enter credit: ")
        credit = int(credit)
        print(f"Your money: {credit}$")
    elif command == "bet":
        bet = input("Bet: ")
        if bet == "all":
            bet = credit
        else:
            bet = int(bet)
        if bet > credit:
            print("You don't have enough money!")
            bet = 0
        else:
            credit -= bet
    elif command == "throw":
        if bet == 0:
            print("You haven\'t bet yet!")
        else:
            val1 = random.randrange(1, 6)
            val2 = random.randrange(1, 6)
            sum1 = val1 + val2
            print("\n - Player 1 has: ", sum1)
            val1 = random.randrange(1, 6)
            val2 = random.randrange(1, 6)
            sum2 = val1 + val2
            print(" - Player 2 has: ", sum2)
            if sum1 == sum2:
                print("Scores are equal. Let's throw again!\n\n")
            elif sum1 > sum2:
                credit = credit + bet * 2
                bet = 0
                print('You won!\n\n')
            else:
                bet = 0
                print("You lost. Try again!\n\n")
    else:
        print("Unknown command!\n\n")