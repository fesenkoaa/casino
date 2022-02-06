"""21: Black Jack"""

import random
import sys, os
from time import sleep

card_deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4 * 2
random.shuffle(card_deck)
# print(card_deck.__len__())

p_credit = 0
c_credit = 1000000000

bet = 0

if card_deck.__len__() <= 10:
    remix = input(f"It's high time to remix card deck.\n"
                  f"The rest is {card_deck.__len__()} cards.\n"
                  f"To remix right now – press ENTER, \nor ANY BUTTON to play: ")
    if remix == '':
        os.system('python3.9 /Applications/casino/casino/21/play_21.py')


while c_credit and card_deck.__len__() >= 10:

    credit_update = True
    while credit_update:
        print(f"Current balance {p_credit}$")
        credit = input("Deposit: ")

        if credit:
            try:
                p_credit += int(credit)
                credit_update = False
            except ValueError:
                print("Invalid item!")

        else:
            credit_update = False

    bet_update = True
    while bet_update:
        print(f"Current bet {bet}$")
        new_bet = input("Bet: ")

        if new_bet == 'all':
            bet = p_credit
            p_credit = 0
            bet_update = False

        elif new_bet:
            try:
                new_bet = int(new_bet)

                if new_bet < p_credit:
                    bet = new_bet
                    p_credit -= bet
                    bet_update = False

                elif new_bet == p_credit:
                    bet = new_bet
                    p_credit = 0
                    bet_update = False

                else:
                    print("\nYou don't have enough money!")
                    print(f"Current balance {p_credit}$")
                    credit = input("Deposit: ")

                    if credit:
                        try:
                            p_credit += int(credit)
                            credit_update = False
                        except ValueError:
                            print("Invalid item!")

            except ValueError:
                print("Invalid item!")

    print(f"\nBANK – {c_credit}$\n\nBALANCE – {p_credit}$\nBET – {bet}$")

    p_score = 0
    c_score = 0

    start = input("\nPress ENTER to play or 'exit' to leave:\n\n")
    if start == '' and bet:

        p_card1 = card_deck.pop()
        p_score += p_card1
        sleep(1)
        print(f"Your first card is {p_card1}.")

        p_card2 = card_deck.pop()
        p_score += p_card2
        sleep(1)
        print(f'Your second card is {p_card2}.')

        if p_score == 21:
            print(f"Wow, {p_score}! My congratulations! You win!\n")
            if bet <= c_credit:
                c_credit -= bet
                p_credit += bet * 2
                bet = 0
            else:
                p_credit += c_credit + bet
                c_credit = 0
                bet = 0

        elif p_score == 22:
            print(f"Wow, {p_score}! My congratulations! You win!\n")
            if bet <= c_credit:
                c_credit -= bet
                p_credit += bet * 2
                bet = 0
            else:
                p_credit += c_credit + bet
                c_credit = 0
                bet = 0

        else:
            c_card1 = card_deck.pop()
            c_score += c_card1
            sleep(1)
            print(f"My first card is {c_card1}.")

            answer1 = input(f"\nYour cards is {p_card1} and {p_card2}, score is {p_score}.\n"
                            f"My first card is {c_card1}. Do you need more?\n"
                            f"ENTER to get or ANY BUTTON if enough:\n\n")
            if answer1 == '':

                p_card3 = card_deck.pop()
                p_score += p_card3
                sleep(1)
                print(f'Your third card is {p_card3}.')

                if p_score == 21:
                    print(f"Wow, {p_score}! My congratulations! You win!\n")
                    if bet <= c_credit:
                        c_credit -= bet
                        p_credit += bet * 2
                        bet = 0
                    else:
                        p_credit += c_credit + bet
                        c_credit = 0
                        bet = 0

                elif p_score > 21:
                    print(f"Oh, {p_score}! You lose!\n")
                    c_credit += bet
                    bet = 0

                else:
                    answer2 = input(f"\nYour cards is {p_card1}, {p_card2} and {p_card3}, score is {p_score}.\n"
                                    f"My first card is {c_card1}. Do you need more?\n"
                                    f"ENTER to get or ANY BUTTON if enough:\n\n")
                    if answer2 == '':

                        p_card4 = card_deck.pop()
                        p_score += p_card4
                        sleep(1)
                        print(f'Your forth card is {p_card4}.')

                        if p_score == 21:
                            print(f"Wow, {p_score}! My congratulations! You win!\n")
                            if bet <= c_credit:
                                c_credit -= bet
                                p_credit += bet * 2
                                bet = 0
                            else:
                                p_credit += c_credit + bet
                                c_credit = 0
                                bet = 0

                        elif p_score > 21:
                            print(f"Oh, {p_score}! You lose!\n")
                            c_credit += bet
                            bet = 0

                        else:
                            answer3 = input(f"\nYour cards is {p_card1}, {p_card2} and {p_card3}, score is {p_score}.\n"
                                            f"My first card is {c_card1}. Do you need more?\n"
                                            f"ENTER to get or ANY BUTTON if enough:\n\n")
                            if answer3 == '':

                                p_card5 = card_deck.pop()
                                p_score += p_card5
                                sleep(1)
                                print(f'Your fifth card is {p_card5}.')

                                if p_score == 21:
                                    print(f"Wow, {p_score}! My congratulations! You win!\n")
                                    if bet <= c_credit:
                                        c_credit -= bet
                                        p_credit += bet * 2
                                        bet = 0
                                    else:
                                        p_credit += c_credit + bet
                                        c_credit = 0
                                        bet = 0

                                elif p_score > 21:
                                    print(f"Oh, {p_score}! You lose!\n")
                                    c_credit += bet
                                    bet = 0

                                else:
                                    print(f"\nYour cards is {p_card1}, {p_card2}, {p_card3}, {p_card4} and {p_card5}"
                                          f", score is {p_score}.\n"
                                          f"We think it's enough for you.\n"
                                          f"My turn!\n\n")

                                    print(f"Total you have {p_score}.")

                                    c_card2 = card_deck.pop()
                                    c_score += c_card2
                                    sleep(1)

                                    if c_score > 22:
                                        print(f"My second card is {c_card2}.")
                                        print(f"My score is {c_score}. You win!\n")
                                        if bet <= c_credit:
                                            c_credit -= bet
                                            p_credit += bet * 2
                                            bet = 0
                                        else:
                                            p_credit += c_credit + bet
                                            c_credit = 0
                                            bet = 0

                                    elif c_score == 22:
                                        print(f"My score is {c_score}. You lose!\n")
                                        c_credit += bet
                                        bet = 0

                                    elif c_score == 21:
                                        print(f"My score is {c_score}. You lose!\n")
                                        c_credit += bet
                                        bet = 0

                                    else:
                                        print(f"My second card is {c_card2}.")

                                        if c_score < p_score:
                                            if c_score < 16:

                                                c_card3 = card_deck.pop()
                                                c_score += c_card3
                                                sleep(1)

                                                if c_score > 21:
                                                    print(f"My second card is {c_card2}.")
                                                    print(f"My score is {c_score}. You win!\n")
                                                    if bet <= c_credit:
                                                        c_credit -= bet
                                                        p_credit += bet * 2
                                                        bet = 0
                                                    else:
                                                        p_credit += c_credit + bet
                                                        c_credit = 0
                                                        bet = 0

                                                elif c_score == 21:
                                                    print(f"My score is {c_score}. You lose!\n")
                                                    c_credit += bet
                                                    bet = 0

                                                else:
                                                    print(f"My third card is {c_card3}.")

                                                    if c_score < p_score:
                                                        if c_score < 15:

                                                            c_card4 = card_deck.pop()
                                                            c_score += c_card4
                                                            sleep(1)

                                                            if c_score > 21:
                                                                print(f"My second card is {c_card2}.")
                                                                print(f"My score is {c_score}. You win!\n")
                                                                if bet <= c_credit:
                                                                    c_credit -= bet
                                                                    p_credit += bet * 2
                                                                    bet = 0
                                                                else:
                                                                    p_credit += c_credit + bet
                                                                    c_credit = 0
                                                                    bet = 0

                                                            elif c_score == 21:
                                                                print(f"My score is {c_score}. You lose!\n")
                                                                c_credit += bet
                                                                bet = 0

                                                            else:
                                                                print(f"My forth card is {c_card4}.")

                                                                if c_score < p_score:
                                                                    if c_score < 14:

                                                                        c_card5 = card_deck.pop()
                                                                        c_score += c_card5
                                                                        sleep(1)

                                                                        if c_score > 21:
                                                                            print(f"My second card is {c_card2}.")
                                                                            print(f"My score is {c_score}. You win!\n")
                                                                            if bet <= c_credit:
                                                                                c_credit -= bet
                                                                                p_credit += bet * 2
                                                                                bet = 0
                                                                            else:
                                                                                p_credit += c_credit + bet
                                                                                c_credit = 0
                                                                                bet = 0

                                                                        elif c_score == 21:
                                                                            print(f"My score is {c_score}. You lose!\n")
                                                                            c_credit += bet
                                                                            bet = 0

                                                                        else:
                                                                            print(f"My fifth card is {c_card5}.")
                                                                            sleep(2)

                                                                            if c_score > p_score:
                                                                                print(
                                                                                    f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                                                c_credit += bet
                                                                                bet = 0

                                                                            elif p_score > c_score:
                                                                                print(
                                                                                    f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                                                if bet <= c_credit:
                                                                                    c_credit -= bet
                                                                                    p_credit += bet * 2
                                                                                    bet = 0
                                                                                else:
                                                                                    p_credit += c_credit + bet
                                                                                    c_credit = 0
                                                                                    bet = 0

                                                                            else:
                                                                                print("Draw!\n")
                                                                                p_credit += bet
                                                                                bet = 0

                                                                    else:
                                                                        sleep(2)

                                                                        if c_score > p_score:
                                                                            print(
                                                                                f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                                            c_credit += bet
                                                                            bet = 0

                                                                        elif p_score > c_score:
                                                                            print(
                                                                                f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                                            if bet <= c_credit:
                                                                                c_credit -= bet
                                                                                p_credit += bet * 2
                                                                                bet = 0
                                                                            else:
                                                                                p_credit += c_credit + bet
                                                                                c_credit = 0
                                                                                bet = 0

                                                                        else:
                                                                            print("Draw!\n")
                                                                            p_credit += bet
                                                                            bet = 0

                                                                else:
                                                                    sleep(2)

                                                                    if c_score > p_score:
                                                                        print(
                                                                            f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                                        c_credit += bet
                                                                        bet = 0

                                                                    else:
                                                                        print("Draw!\n")
                                                                        p_credit += bet
                                                                        bet = 0

                                                        else:
                                                            sleep(2)

                                                            if c_score > p_score:
                                                                print(
                                                                    f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                                c_credit += bet
                                                                bet = 0

                                                            elif p_score > c_score:
                                                                print(
                                                                    f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                                if bet <= c_credit:
                                                                    c_credit -= bet
                                                                    p_credit += bet * 2
                                                                    bet = 0
                                                                else:
                                                                    p_credit += c_credit + bet
                                                                    c_credit = 0
                                                                    bet = 0

                                                            else:
                                                                print("Draw!\n")
                                                                p_credit += bet
                                                                bet = 0

                                                    else:
                                                        sleep(2)

                                                        if c_score > p_score:
                                                            print(
                                                                f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                            c_credit -= bet
                                                            bet = 0

                                                        else:
                                                            print("Draw!\n")
                                                            p_credit += bet
                                                            bet = 0

                                            else:
                                                sleep(2)

                                                if c_score > p_score:
                                                    print(f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                    c_credit += bet
                                                    bet = 0

                                                elif p_score > c_score:
                                                    print(f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                    if bet <= c_credit:
                                                        c_credit -= bet
                                                        p_credit += bet * 2
                                                        bet = 0
                                                    else:
                                                        p_credit += c_credit + bet
                                                        c_credit = 0
                                                        bet = 0

                                                else:
                                                    print("Draw!\n")
                                                    p_credit += bet
                                                    bet = 0

                                        else:
                                            sleep(2)
                                            if c_score > p_score:
                                                print(f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                c_credit += bet
                                                bet = 0

                                            else:
                                                print("Draw!\n")
                                                p_credit += bet
                                                bet = 0

                            elif answer3:

                                print(f"Total you have {p_score}.")

                                c_card2 = card_deck.pop()
                                c_score += c_card2
                                sleep(1)

                                if c_score > 22:
                                    print(f"My second card is {c_card2}.")
                                    print(f"My score is {c_score}. You win!\n")
                                    if bet <= c_credit:
                                        c_credit -= bet
                                        p_credit += bet * 2
                                        bet = 0
                                    else:
                                        p_credit += c_credit + bet
                                        c_credit = 0
                                        bet = 0

                                elif c_score == 22:
                                    print(f"My second card is {c_card2}.")
                                    print(f"My score is {c_score}. You lose!\n")
                                    c_credit += bet
                                    bet = 0

                                elif c_score == 21:
                                    print(f"My second card is {c_card2}.")
                                    print(f"My score is {c_score}. You lose!\n")
                                    c_credit -= bet
                                    p_credit += bet * 2
                                    bet = 0

                                else:
                                    print(f"My second card is {c_card2}.")

                                    if c_score < p_score:
                                        if c_score < 16:

                                            c_card3 = card_deck.pop()
                                            c_score += c_card3
                                            sleep(1)

                                            if c_score > 21:
                                                print(f"My third card is {c_card2}.")
                                                print(f"My score is {c_score}. You win!\n")
                                                if bet <= c_credit:
                                                    c_credit -= bet
                                                    p_credit += bet * 2
                                                    bet = 0
                                                else:
                                                    p_credit += c_credit + bet
                                                    c_credit = 0
                                                    bet = 0

                                            elif c_score == 21:
                                                print(f"My third card is {c_card2}.")
                                                print(f"My score is {c_score}. You lose!\n")
                                                c_credit += bet
                                                bet = 0

                                            else:
                                                print(f"My third card is {c_card3}.")

                                                if c_score < p_score:
                                                    if c_score < 15:

                                                        c_card4 = card_deck.pop()
                                                        c_score += c_card4
                                                        sleep(1)

                                                        if c_score > 21:
                                                            print(f"My forth card is {c_card2}.")
                                                            print(f"My score is {c_score}. You win!\n")
                                                            if bet <= c_credit:
                                                                c_credit -= bet
                                                                p_credit += bet * 2
                                                                bet = 0
                                                            else:
                                                                p_credit += c_credit + bet
                                                                c_credit = 0
                                                                bet = 0

                                                        elif c_score == 21:
                                                            print(f"My forth card is {c_card2}.")
                                                            print(f"My score is {c_score}. You lose!\n")
                                                            c_credit += bet
                                                            bet = 0

                                                        else:
                                                            print(f"My forth card is {c_card4}.")

                                                            if c_score < p_score:
                                                                if c_score < 14:

                                                                    c_card5 = card_deck.pop()
                                                                    c_score += c_card5
                                                                    sleep(1)

                                                                    if c_score > 21:
                                                                        print(f"My fifth card is {c_card2}.")
                                                                        print(f"My score is {c_score}. You win!\n")
                                                                        if bet <= c_credit:
                                                                            c_credit -= bet
                                                                            p_credit += bet * 2
                                                                            bet = 0
                                                                        else:
                                                                            p_credit += c_credit + bet
                                                                            c_credit = 0
                                                                            bet = 0

                                                                    elif c_score == 21:
                                                                        print(f"My fifth card is {c_card2}.")
                                                                        print(f"My score is {c_score}. You lose!\n")
                                                                        c_credit += bet
                                                                        bet = 0

                                                                    else:
                                                                        print(f"My fifth card is {c_card5}.")
                                                                        sleep(2)

                                                                        if c_score > p_score:
                                                                            print(
                                                                                f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                                            c_credit += bet
                                                                            bet = 0

                                                                        elif p_score > c_score:
                                                                            print(
                                                                                f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                                            if bet <= c_credit:
                                                                                c_credit -= bet
                                                                                p_credit += bet * 2
                                                                                bet = 0
                                                                            else:
                                                                                p_credit += c_credit + bet
                                                                                c_credit = 0
                                                                                bet = 0

                                                                        else:
                                                                            print("Draw!\n")
                                                                            p_credit += bet
                                                                            bet = 0

                                                                else:
                                                                    sleep(2)

                                                                    if c_score > p_score:
                                                                        print(
                                                                            f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                                        c_credit += bet
                                                                        bet = 0

                                                                    elif p_score > c_score:
                                                                        print(
                                                                            f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                                        if bet <= c_credit:
                                                                            c_credit -= bet
                                                                            p_credit += bet * 2
                                                                            bet = 0
                                                                        else:
                                                                            p_credit += c_credit + bet
                                                                            c_credit = 0
                                                                            bet = 0

                                                                    else:
                                                                        print("Draw!\n")
                                                                        p_credit += bet
                                                                        bet = 0

                                                            else:
                                                                sleep(2)

                                                                if c_score > p_score:
                                                                    print(
                                                                        f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                                    c_credit += bet
                                                                    bet = 0

                                                                else:
                                                                    print("Draw!\n")
                                                                    p_credit += bet
                                                                    bet = 0

                                                    else:
                                                        sleep(2)

                                                        if c_score > p_score:
                                                            print(
                                                                f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                            c_credit += bet
                                                            bet = 0

                                                        elif p_score > c_score:
                                                            print(
                                                                f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                            if bet <= c_credit:
                                                                c_credit -= bet
                                                                p_credit += bet * 2
                                                                bet = 0
                                                            else:
                                                                p_credit += c_credit + bet
                                                                c_credit = 0
                                                                bet = 0

                                                        else:
                                                            print("Draw!\n")
                                                            p_credit += bet
                                                            bet = 0

                                                else:
                                                    sleep(2)

                                                    if c_score > p_score:
                                                        print(
                                                            f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                        c_credit += bet
                                                        bet = 0

                                                    else:
                                                        print("Draw!\n")
                                                        p_credit += bet
                                                        bet = 0

                                        else:
                                            sleep(2)

                                            if c_score > p_score:
                                                print(f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                c_credit += bet
                                                bet = 0

                                            elif p_score > c_score:
                                                print(f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                if bet <= c_credit:
                                                    c_credit -= bet
                                                    p_credit += bet * 2
                                                    bet = 0
                                                else:
                                                    p_credit += c_credit + bet
                                                    c_credit = 0
                                                    bet = 0

                                            else:
                                                print("Draw!\n")
                                                p_credit += bet
                                                bet = 0

                                    else:
                                        sleep(2)
                                        if c_score > p_score:
                                            print(f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                            c_credit += bet
                                            bet = 0

                                        else:
                                            print("Draw!\n")
                                            p_credit += bet
                                            bet = 0

                    elif answer2:

                        print(f"Total you have {p_score}.")

                        c_card2 = card_deck.pop()
                        c_score += c_card2
                        sleep(1)

                        if c_score > 22:
                            print(f"My second card is {c_card2}.")
                            print(f"My score is {c_score}. You win!\n")
                            if bet <= c_credit:
                                c_credit -= bet
                                p_credit += bet * 2
                                bet = 0
                            else:
                                p_credit += c_credit + bet
                                c_credit = 0
                                bet = 0

                        elif c_score == 22:
                            print(f"My second card is {c_card2}.")
                            print(f"My score is {c_score}. You lose!\n")
                            c_credit -= bet
                            bet = 0

                        elif c_score == 21:
                            print(f"My second card is {c_card2}.")
                            print(f"My score is {c_score}. You lose!\n")
                            c_credit += bet
                            bet = 0

                        else:
                            print(f"My second card is {c_card2}.")

                            if c_score < p_score:
                                if c_score < 16:

                                    c_card3 = card_deck.pop()
                                    c_score += c_card3
                                    sleep(1)

                                    if c_score > 21:
                                        print(f"My third card is {c_card2}.")
                                        print(f"My score is {c_score}. You win!\n")
                                        if bet <= c_credit:
                                            c_credit -= bet
                                            p_credit += bet * 2
                                            bet = 0
                                        else:
                                            p_credit += c_credit + bet
                                            c_credit = 0
                                            bet = 0

                                    elif c_score == 21:
                                        print(f"My third card is {c_card2}.")
                                        print(f"My score is {c_score}. You lose!\n")
                                        c_credit += bet
                                        bet = 0

                                    else:
                                        print(f"My third card is {c_card3}.")

                                        if c_score < p_score:
                                            if c_score < 15:

                                                c_card4 = card_deck.pop()
                                                c_score += c_card4
                                                sleep(1)

                                                if c_score > 21:
                                                    print(f"My firth card is {c_card2}.")
                                                    print(f"My score is {c_score}. You win!\n")
                                                    if bet <= c_credit:
                                                        c_credit -= bet
                                                        p_credit += bet * 2
                                                        bet = 0
                                                    else:
                                                        p_credit += c_credit + bet
                                                        c_credit = 0
                                                        bet = 0

                                                elif c_score == 21:
                                                    print(f"My firth card is {c_card2}.")
                                                    print(f"My score is {c_score}. You lose!\n")
                                                    c_credit += bet
                                                    bet = 0

                                                else:
                                                    print(f"My forth card is {c_card4}.")

                                                    if c_score < p_score:
                                                        if c_score < 14:

                                                            c_card5 = card_deck.pop()
                                                            c_score += c_card5
                                                            sleep(1)

                                                            if c_score > 21:
                                                                print(f"My fifth card is {c_card2}.")
                                                                print(f"My score is {c_score}. You win!\n")
                                                                if bet <= c_credit:
                                                                    c_credit -= bet
                                                                    p_credit += bet * 2
                                                                    bet = 0
                                                                else:
                                                                    p_credit += c_credit + bet
                                                                    c_credit = 0
                                                                    bet = 0

                                                            elif c_score == 21:
                                                                print(f"My fifth card is {c_card2}.")
                                                                print(f"My score is {c_score}. You lose!\n")
                                                                c_credit += bet
                                                                bet = 0

                                                            else:
                                                                print(f"My fifth card is {c_card5}.")
                                                                sleep(2)

                                                                if c_score > p_score:
                                                                    print(
                                                                        f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                                    c_credit += bet
                                                                    bet = 0

                                                                elif p_score > c_score:
                                                                    print(
                                                                        f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                                    if bet <= c_credit:
                                                                        c_credit -= bet
                                                                        p_credit += bet * 2
                                                                        bet = 0
                                                                    else:
                                                                        p_credit += c_credit + bet
                                                                        c_credit = 0
                                                                        bet = 0

                                                                else:
                                                                    print("Draw!\n")
                                                                    p_credit += bet
                                                                    bet = 0

                                                        else:
                                                            sleep(2)

                                                            if c_score > p_score:
                                                                print(
                                                                    f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                                c_credit += bet
                                                                bet = 0

                                                            elif p_score > c_score:
                                                                print(
                                                                    f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                                if bet <= c_credit:
                                                                    c_credit -= bet
                                                                    p_credit += bet * 2
                                                                    bet = 0
                                                                else:
                                                                    p_credit += c_credit + bet
                                                                    c_credit = 0
                                                                    bet = 0

                                                            else:
                                                                print("Draw!\n")
                                                                p_credit += bet
                                                                bet = 0

                                                    else:
                                                        sleep(2)

                                                        if c_score > p_score:
                                                            print(
                                                                f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                            c_credit += bet
                                                            bet = 0

                                                        else:
                                                            print("Draw!")
                                                            p_credit += bet
                                                            bet = 0

                                            else:
                                                sleep(2)

                                                if c_score > p_score:
                                                    print(
                                                        f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                    c_credit += bet
                                                    bet = 0

                                                elif p_score > c_score:
                                                    print(
                                                        f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                    if bet <= c_credit:
                                                        c_credit -= bet
                                                        p_credit += bet * 2
                                                        bet = 0
                                                    else:
                                                        p_credit += c_credit + bet
                                                        c_credit = 0
                                                        bet = 0

                                                else:
                                                    print("Draw!\n")
                                                    p_credit += bet
                                                    bet = 0

                                        else:
                                            sleep(2)

                                            if c_score > p_score:
                                                print(f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                c_credit += bet
                                                bet = 0

                                            else:
                                                print("Draw!\n")
                                                p_credit += bet
                                                bet = 0

                                else:
                                    sleep(2)

                                    if c_score > p_score:
                                        print(f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                        c_credit += bet
                                        bet = 0

                                    elif p_score > c_score:
                                        print(f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                        if bet <= c_credit:
                                            c_credit -= bet
                                            p_credit += bet * 2
                                            bet = 0
                                        else:
                                            p_credit += c_credit + bet
                                            c_credit = 0
                                            bet = 0

                                    else:
                                        print("Draw!\n")
                                        p_credit += bet
                                        bet = 0

                            else:
                                sleep(2)
                                if c_score > p_score:
                                    print(f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                    c_credit += bet
                                    bet = 0

                                else:
                                    print("Draw!\n")
                                    p_credit += bet
                                    bet = 0

            elif answer1:

                print(f"Total you have {p_score}.")

                c_card2 = card_deck.pop()
                c_score += c_card2
                sleep(1)

                if c_score > 22:
                    print(f"My second card is {c_card2}.")
                    print(f"My score is {c_score}. You win!\n")
                    if bet <= c_credit:
                        c_credit -= bet
                        p_credit += bet * 2
                        bet = 0
                    else:
                        p_credit += c_credit + bet
                        c_credit = 0
                        bet = 0

                elif c_score == 22:
                    print(f"My second card is {c_card2}.")
                    print(f"My score is {c_score}. You lose!\n")
                    c_credit += bet
                    bet = 0

                elif c_score == 21:
                    print(f"My second card is {c_card2}.")
                    print(f"My score is {c_score}. You lose!\n")
                    c_credit += bet
                    bet = 0

                else:
                    print(f"My second card is {c_card2}.")

                    if c_score < p_score:
                        if c_score < 16:

                            c_card3 = card_deck.pop()
                            c_score += c_card3
                            sleep(1)

                            if c_score > 21:
                                print(f"My third card is {c_card2}.")
                                print(f"My score is {c_score}. You win!\n")
                                if bet <= c_credit:
                                    c_credit -= bet
                                    p_credit += bet * 2
                                    bet = 0
                                else:
                                    p_credit += c_credit + bet
                                    c_credit = 0
                                    bet = 0

                            elif c_score == 21:
                                print(f"My third card is {c_card2}.")
                                print(f"My score is {c_score}. You lose!\n")
                                c_credit += bet
                                bet = 0

                            else:
                                print(f"My third card is {c_card3}.")

                                if c_score < p_score:
                                    if c_score < 15:

                                        c_card4 = card_deck.pop()
                                        c_score += c_card4
                                        sleep(1)

                                        if c_score > 21:
                                            print(f"My forth card is {c_card2}.")
                                            print(f"My score is {c_score}. You win!\n")
                                            if bet <= c_credit:
                                                c_credit -= bet
                                                p_credit += bet * 2
                                                bet = 0
                                            else:
                                                p_credit += c_credit + bet
                                                c_credit = 0
                                                bet = 0

                                        elif c_score == 21:
                                            print(f"My forth card is {c_card2}.")
                                            print(f"My score is {c_score}. You lose!\n")
                                            c_credit += bet
                                            bet = 0

                                        else:
                                            print(f"My forth card is {c_card4}.")

                                            if c_score < p_score:
                                                if c_score < 14:

                                                    c_card5 = card_deck.pop()
                                                    c_score += c_card5
                                                    sleep(1)

                                                    if c_score > 21:
                                                        print(f"My fifth card is {c_card2}.")
                                                        print(f"My score is {c_score}. You win!\n")
                                                        if bet <= c_credit:
                                                            c_credit -= bet
                                                            p_credit += bet * 2
                                                            bet = 0
                                                        else:
                                                            p_credit += c_credit + bet
                                                            c_credit = 0
                                                            bet = 0

                                                    elif c_score == 21:
                                                        print(f"My fifth card is {c_card2}.")
                                                        print(f"My score is {c_score}. You lose!\n")
                                                        c_credit += bet
                                                        bet = 0

                                                    else:
                                                        print(f"My fifth card is {c_card5}.")
                                                        sleep(2)

                                                        if c_score > p_score:
                                                            print(
                                                                f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                            c_credit += bet
                                                            bet = 0

                                                        elif p_score > c_score:
                                                            print(
                                                                f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                            if bet <= c_credit:
                                                                c_credit -= bet
                                                                p_credit += bet * 2
                                                                bet = 0
                                                            else:
                                                                p_credit += c_credit + bet
                                                                c_credit = 0
                                                                bet = 0

                                                        else:
                                                            print("Draw!\n")
                                                            p_credit += bet
                                                            bet = 0

                                                else:
                                                    sleep(2)

                                                    if c_score > p_score:
                                                        print(
                                                            f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                        c_credit += bet
                                                        bet = 0

                                                    elif p_score > c_score:
                                                        print(
                                                            f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                                        if bet <= c_credit:
                                                            c_credit -= bet
                                                            p_credit += bet * 2
                                                            bet = 0
                                                        else:
                                                            p_credit += c_credit + bet
                                                            c_credit = 0
                                                            bet = 0

                                                    else:
                                                        print("Draw!\n")
                                                        p_credit += bet
                                                        bet = 0

                                            else:
                                                sleep(2)

                                                if c_score > p_score:
                                                    print(
                                                        f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                                    c_credit += bet
                                                    bet = 0

                                                else:
                                                    print("Draw!\n")
                                                    p_credit += bet
                                                    bet = 0

                                    else:
                                        sleep(2)

                                        if c_score > p_score:
                                            print(
                                                f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                            c_credit += bet
                                            bet = 0

                                        elif p_score > c_score:
                                            print(
                                                f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                            if bet <= c_credit:
                                                c_credit -= bet
                                                p_credit += bet * 2
                                                bet = 0
                                            else:
                                                p_credit += c_credit + bet
                                                c_credit = 0
                                                bet = 0

                                        else:
                                            print("Draw!\n")
                                            p_credit += bet
                                            bet = 0

                                else:
                                    sleep(2)

                                    if c_score > p_score:
                                        print(f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                        c_credit += bet
                                        bet = 0

                                    else:
                                        print("Draw!\n")
                                        p_credit += bet
                                        bet = 0

                        else:
                            sleep(2)

                            if c_score > p_score:
                                print(f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                                c_credit += bet
                                bet = 0

                            elif p_score > c_score:
                                print(f"Enough! My score is {c_score}, your - {p_score}. You win!\n")
                                if bet <= c_credit:
                                    c_credit -= bet
                                    p_credit += bet * 2
                                    bet = 0
                                else:
                                    p_credit += c_credit + bet
                                    c_credit = 0
                                    bet = 0

                            else:
                                print("Draw!\n")
                                p_credit += bet
                                bet = 0

                    else:
                        sleep(2)
                        if c_score > p_score:
                            print(f"Enough! My score is {c_score}, your - {p_score}. You lose!\n")
                            c_credit += bet
                            bet = 0

                        else:
                            print("Draw!\n")
                            p_credit += bet
                            bet = 0

    elif start == 'exit':
        sys.exit()
    else:
        print('Unknown command!')