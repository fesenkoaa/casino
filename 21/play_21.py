"""21: Black Jack"""

import random
import sys
from time import sleep
from croupier_21 import croupier_play as croupier

card_deck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4 * 2
random.shuffle(card_deck)

p_credit = 0
c_credit = 0

while True:

    p_score = 0
    c_score = 0

    start = input("\nWould you like to play Black Jack?\n"
                  "'yes' to play or 'exit' to leave:\n\n")
    if start == 'yes':

        p_card1 = card_deck.pop()
        p_score += p_card1
        sleep(1)
        print(f"Your first card is {p_card1}.")

        p_card2 = card_deck.pop()
        p_score += p_card2
        sleep(1)
        print(f'Your second card is {p_card2}.')

        if p_score == 21:
            print(f"Wow, {p_score}! My congratulations! You won!")
        elif p_score == 22:
            print(f"Wow, {p_score}! My congratulations! You won!")
        else:
            c_card1 = card_deck.pop()
            c_score += c_card1
            sleep(1)
            print(f"My first card is {c_card1}.")

            answer1 = input(f"\nYour cards is {p_card1} and {p_card2}, score is {p_score}.\n"
                            f"My first card is {c_card1}. Do you need more?\n"
                            f"'get' to get or 'stop' if enough:\n\n")
            if answer1 == 'get':

                p_card3 = card_deck.pop()
                p_score += p_card3
                sleep(1)
                print(f'Your second card is {p_card3}.')

                if p_score == 21:
                    print(f"Wow, {p_score}! My congratulations! You won!")
                elif p_score > 21:
                    print(f"Oh, {p_score}! You lose!")
                else:
                    answer2 = input(f"\nYour cards is {p_card1}, {p_card2} and {p_card3}, score is {p_score}.\n"
                                    f"My first card is {c_card1}. Do you need more?\n"
                                    f"'get' to get or 'stop' if enough:\n\n")
                    if answer2 == 'get':

                        p_card4 = card_deck.pop()
                        p_score += p_card4
                        sleep(1)
                        print(f'Your second card is {p_card4}.')

                        if p_score == 21:
                            print(f"Wow, {p_score}! My congratulations! You won!")
                        elif p_score > 21:
                            print(f"Oh, {p_score}! You lose!")
                        else:
                            answer3 = input(f"\nYour cards is {p_card1}, {p_card2} and {p_card3}, score is {p_score}.\n"
                                            f"My first card is {c_card1}. Do you need more?\n"
                                            f"'get' to get or 'stop' if enough:\n\n")
                            if answer3 == 'get':

                                p_card5 = card_deck.pop()
                                p_score += p_card5
                                sleep(1)
                                print(f'Your second card is {p_card5}.')

                                if p_score == 21:
                                    print(f"Wow, {p_score}! My congratulations! You won!")
                                elif p_score > 21:
                                    print(f"Oh, {p_score}! You lose!")
                                else:
                                    print(f"\nYour cards is {p_card1}, {p_card2}, {p_card3}, {p_card4} and {p_card5}"
                                          f", score is {p_score}.\n"
                                          f"We think it's enough for you.\n"
                                          f"My turn!\n\n")

                                    winner = ''
                                    croupier(c_score, p_score, card_deck)
                                    if winner == 'croupier':
                                        print(f"Croupier wins! Score: {c_score} against {p_score}")
                                        c_score = 0
                                        p_score = 0
                                    elif winner == 'player':
                                        print(f"You wins! Score: {p_score} against {c_score}")
                                        c_score = 0
                                        p_score = 0
                                    elif winner == 'nobody':
                                        print(f"Draw!")
                                        c_score = 0
                                        p_score = 0

                            elif answer3 == 'stop':

                                winner = ''
                                croupier(c_score, p_score, card_deck)
                                if winner == 'croupier':
                                    print(f"Croupier wins! Score: {c_score} against {p_score}")
                                    c_score = 0
                                    p_score = 0
                                elif winner == 'player':
                                    print(f"You wins! Score: {p_score} against {c_score}")
                                    c_score = 0
                                    p_score = 0
                                elif winner == 'nobody':
                                    print(f"Draw!")
                                    c_score = 0
                                    p_score = 0

                    elif answer2 == 'stop':

                        winner = ''
                        croupier(c_score, p_score, card_deck)
                        if winner == 'croupier':
                            print(f"Croupier wins! Score: {c_score} against {p_score}")
                            c_score = 0
                            p_score = 0
                        elif winner == 'player':
                            print(f"You wins! Score: {p_score} against {c_score}")
                            c_score = 0
                            p_score = 0
                        elif winner == 'nobody':
                            print(f"Draw!")
                            c_score = 0
                            p_score = 0

            elif answer1 == 'stop':

                winner = ''
                croupier(c_score, p_score, card_deck)
                if winner == 'croupier':
                    print(f"Croupier wins! Score: {c_score} against {p_score}")
                    c_score = 0
                    p_score = 0
                elif winner == 'player':
                    print(f"You wins! Score: {p_score} against {c_score}")
                    c_score = 0
                    p_score = 0
                elif winner == 'nobody':
                    print(f"Draw!")
                    c_score = 0
                    p_score = 0

