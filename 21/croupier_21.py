""" CROUPIER'S LOGIC """

from time import sleep


def croupier_play(croupier_score, player_score, cards):
    print(f"Total you have {player_score}.")

    c_card2 = cards.pop()
    croupier_score += c_card2
    sleep(1)
    if croupier_score > 22:
        print(f"My second card is {c_card2}.")
        print(f"My score is {croupier_score}. You win!")
        winner = 'player'
        return winner
    elif croupier_score == 22:
        print(f"My score is {croupier_score}. You lose!")
        winner = 'croupier'
        return winner
    elif croupier_score == 21:
        print(f"My score is {croupier_score}. You lose!")
        winner = 'croupier'
        return winner
    else:
        print(f"My second card is {c_card2}.")
        if croupier_score < player_score:
            if croupier_score < 16:

                c_card3 = cards.pop()
                croupier_score += c_card3
                sleep(1)
                if croupier_score > 21:
                    print(f"My second card is {c_card2}.")
                    print(f"My score is {croupier_score}. You win!")
                    winner = 'player'
                    return winner
                elif croupier_score == 21:
                    print(f"My score is {croupier_score}. You lose!")
                    winner = 'croupier'
                    return winner
                else:
                    print(f"My third card is {c_card3}.")
                    if croupier_score < player_score:
                        if croupier_score < 15:

                            c_card4 = cards.pop()
                            croupier_score += c_card4
                            sleep(1)
                            if croupier_score > 21:
                                print(f"My second card is {c_card2}.")
                                print(f"My score is {croupier_score}. You win!")
                                winner = 'player'
                                return winner
                            elif croupier_score == 21:
                                print(f"My score is {croupier_score}. You lose!")
                                winner = 'croupier'
                                return winner
                            else:
                                print(f"My forth card is {c_card4}.")
                                if croupier_score < player_score:
                                    if croupier_score < 14:

                                        c_card5 = cards.pop()
                                        croupier_score += c_card5
                                        sleep(1)
                                        if croupier_score > 21:
                                            print(f"My second card is {c_card2}.")
                                            print(f"My score is {croupier_score}. You win!")
                                            winner = 'player'
                                            return winner
                                        elif croupier_score == 21:
                                            print(f"My score is {croupier_score}. You lose!")
                                            winner = 'croupier'
                                            return winner
                                        else:
                                            print(f"My fifth card is {c_card5}.")

                                            sleep(2)
                                            if croupier_score > player_score:
                                                print(f"Enough! My score is {croupier_score}, your - {player_score}. You lose!")
                                                winner = 'croupier'
                                            elif player_score > croupier_score:
                                                print(f"Enough! My score is {croupier_score}, your - {player_score}. You win!")
                                                winner = 'player'
                                            else:
                                                print("Draw!")
                                                winner = 'nobody'
                                            return winner

                                    else:

                                        sleep(2)
                                        if croupier_score > player_score:
                                            print(f"Enough! My score is {croupier_score}, your - {player_score}. You lose!")
                                            winner = 'croupier'
                                        elif player_score > croupier_score:
                                            print(f"Enough! My score is {croupier_score}, your - {player_score}. You win!")
                                            winner = 'player'
                                        else:
                                            print("Draw!")
                                            winner = 'nobody'
                                        return winner

                                else:
                                    sleep(2)
                                    if croupier_score > player_score:
                                        print(f"Enough! My score is {croupier_score}, your - {player_score}. You lose!")
                                        winner = 'croupier'
                                    else:
                                        print("Draw!")
                                        winner = 'nobody'
                                    return winner

                        else:

                            sleep(2)
                            if croupier_score > player_score:
                                print(f"Enough! My score is {croupier_score}, your - {player_score}. You lose!")
                                winner = 'croupier'
                            elif player_score > croupier_score:
                                print(f"Enough! My score is {croupier_score}, your - {player_score}. You win!")
                                winner = 'player'
                            else:
                                print("Draw!")
                                winner = 'nobody'
                            return winner

                    else:
                        sleep(2)
                        if croupier_score > player_score:
                            print(f"Enough! My score is {croupier_score}, your - {player_score}. You lose!")
                            winner = 'croupier'
                        else:
                            print("Draw!")
                            winner = 'nobody'
                        return winner

            else:

                sleep(2)
                if croupier_score > player_score:
                    print(f"Enough! My score is {croupier_score}, your - {player_score}. You lose!")
                    winner = 'croupier'
                elif player_score > croupier_score:
                    print(f"Enough! My score is {croupier_score}, your - {player_score}. You win!")
                    winner = 'player'
                else:
                    print("Draw!")
                    winner = 'nobody'
                return winner

        else:
            sleep(2)
            if croupier_score > player_score:
                print(f"Enough! My score is {croupier_score}, your - {player_score}. You lose!")
                winner = 'croupier'
            else:
                print("Draw!")
                winner = 'nobody'
            return winner


# cards = [1, 3, 7, 7, 3, 5, 2, 8, 1, 4]
# c_score = 6
# p_score = 16
#
# croupier_play(c_score, p_score, cards)