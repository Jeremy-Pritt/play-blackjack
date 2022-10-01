# import packages and classes
import random
from DeckOfCards import DeckOfCards

# create sentinel to allow them to keep playing
playing = True

# if they are still playing...
while playing == True:

    # generate a dealer score between 17 and 23
    dealer_score = random.randint(17, 23)

    # generate a deck of cards and print
    deck = DeckOfCards()

    # welcome user to Black Jack
    print("Welcome to Black Jack!")
    print()

    # print unshuffled deck
    deck.print_deck()
    print()

    # shuffle the deck of cards and print
    deck.shuffle_deck()
    deck.print_deck()
    print()

    # deal two cards to the user
    card = deck.get_card()
    card2 = deck.get_card()

    # calculate the user's hand score and print
    score = 0
    score += card.val
    score += card2.val
    print("Your score is: ", score)
    print()

    # assign x to True to work as a sentinel in while loop
    x = True

    # keep asking the user if they want to hit until they decline or bust
    while x == True and score < 21:
        hit = input("Would you like a hit?(y/n): ")

        # control for if the user input is weird
        if hit not in ['y', 'n']:
            print("Please input 'y' for 'yes' and 'n' for 'no'")
            continue

        # hit the player again if they choose to hit again
        elif hit == 'y':
            new_card = deck.get_card()
            score += new_card.val
            print("New Score: ", score)
            if score > 21:
                x = False

        # end the game if they decline to hit
        else:
            x = False
            print()

    # end the game if they have busted
    if score > 21:
        print()
        print("You busted, Dealer wins!")

        # prompt the player to play again
        print()
        play_again = input("Press 'y' to play again! Press 'n' to quit: ")

        # restart the game if they say yes; quit if they say no
        if play_again == 'y':
            continue
        else:
            playing = False
            continue

    # print dealer score
    print("Dealer score is: " + str(dealer_score))

    # provide logic depending on if the user won or loss
    print()
    if dealer_score > 21 and score <= 21:
        print("Dealer Busted, you win!!!")
    elif dealer_score > score:
        print("Dealer score is higher, you lose!")
    elif dealer_score == 21 == score:
        print("You tied with the dealer!")
    elif dealer_score == score:
        ("Your scores are equal, but you lose!")
    else:
        print("Your score is higher, you win!!!")

    # prompt the player to play again
    print()
    play_again = input("Press 'y' to play again! Press 'n' to quit: ")

    # restart the game if they say yes; quit if they say no
    if play_again == 'y':
        continue
    else:
        playing = False
