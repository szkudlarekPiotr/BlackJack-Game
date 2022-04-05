import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
users_hand = []
computers_hand = []


def first_deal():
    users_hand.clear()
    computers_hand.clear()
    for n in range(0, 2):
        users_hand.append(random.choice(cards))
    computers_hand.append(random.choice(cards))
    print(f"Your cards: {users_hand}, current score: {sum(users_hand)} \nComputer's first card: {computers_hand}")
    draw()


def draw():
    stop_drawing = False
    while not stop_drawing:
        question = input("Do you want to draw another card? Type 'y' or 'n': ")
        if question.lower() == 'y':
            users_hand.append(random.choice(cards))
            if 11 in users_hand and sum(users_hand) > 21:
                users_hand[users_hand.index(11)] = 1
            print(f"Your cards: {users_hand}, current score: {sum(users_hand)} \nComputer's first card: {computers_hand}")
            if (sum(users_hand)) > 21:
                stop_drawing = True
                print('You went over, you lose!')
        else:
            computers_turn = True
            stop_drawing = True
            computers_hand.append(random.choice(cards))
            while computers_turn:
                if sum(computers_hand) < sum(users_hand) or sum(computers_hand) < 17:
                    card = random.choice(cards)
                    if card == 11 and sum(computers_hand) + card > 21:
                        card = 1
                    computers_hand.append(card)
                else:
                    computers_turn = False
            print(
                f"Your final hand: {users_hand}, final score: {sum(users_hand)} \nComputer's final hand {computers_hand}, final score {sum(computers_hand)}")
            determine_winner()


def determine_winner():
    users_score = sum(users_hand)
    computers_score = sum(computers_hand)
    if users_score > computers_score or computers_score > 21:
        print("You won!")
    elif users_score == computers_score:
        print('Draw!')
    elif computers_score > users_score:
        print('Computer won!')


restart = True
while restart:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start_game.lower() == 'y':
        print(logo)
        first_deal()
    else:
        restart = False
