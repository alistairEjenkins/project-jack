import time
import random
from os import system, name

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A',
            '2','3','4','5','6','7','8','9','10','J','Q','K','A',
            '2','3','4','5','6','7','8','9','10','J','Q','K','A',
            '2','3','4','5','6','7','8','9','10','J','Q','K','A',]

cards_dealt = {'player': [],'dealer': [],}
scores = {'player' : 0, 'dealer' : 0}

def setup():
    global deck, cards_dealt, scores

    deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A',
            '2','3','4','5','6','7','8','9','10','J','Q','K','A',
            '2','3','4','5','6','7','8','9','10','J','Q','K','A',
            '2','3','4','5','6','7','8','9','10','J','Q','K','A',]

    cards_dealt = {'player': [],'dealer': [],}
    scores = {'player' : 0, 'dealer' : 0}

def clear(): # clear the screen
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def total_score(competitor, dealt, score = 0):

    total = 0
    already_got_ace = False

    for card in dealt:
        if card == 'A': # determing points scored for an ace
            if competitor == 'player':
                print('Do you want your ace to count as 1 or 11?')
                total +=int(input('> '))
            else:
                if 'A' in dealt and not already_got_ace: # dealers first ace in hand always count ''
                                                            # as 11, subsequent aces count as 1
                    already_got_ace = True
                    total += 11
                else:
                    total += 1
        elif str(card) in 'JQK': # 10 points for a picture card
            total += 10
        else:
            total += int(card) # n number points for number card
    total += score
    # display complete hand and score
    print(f"{competitor}'s hand: {display_hand(competitor)} score: {total}")
    return total


def determine_winner(competitor, score=-10): # dummy score used to set players score as
                                                # high score on completing their hand

    scores[competitor] = score

    high_score = -20
    for competitor, score in scores.items():
        if scores[competitor] > high_score:
            high_score = score
            winner = competitor
        elif scores[competitor] == high_score:
            winner = 'tie'
    return winner


def add_card_to_hand(competitor, score):
    new_card = deal_card()
    cards_dealt[competitor].append(new_card)
    return total_score(competitor, [new_card], score) # determine competitors score
                                                        # by adding score of new card
                                                        # to their existing score.


def complete_hand(competitor):

    completing_hand = True
    # calculate total for each person playing
    score = total_score(competitor, cards_dealt[competitor])
    # complete hand for ...
    while completing_hand and score <= 21:
        if competitor == 'player': # ... the player
            print('Do you want to hit (h) or stand (s)?')
            choice = input('> ')
            if choice == 'h':
                # score += points for new card dealt to player
                score = add_card_to_hand('player',score)
            else:
                completing_hand = False
        else:
            if score < 17: # ... the dealer, hit if score less than 17
                # score += points for new card dealt to player
                score = add_card_to_hand('dealer', score)
            else:
                completing_hand = False
    else:
        if score > 21:
            print('busted!')
            winner = determine_winner(competitor) # if someone has busted
        else:
            winner = determine_winner(competitor, score)
    return winner


def display_hand(competitor):

    return ', '.join(cards_dealt[competitor])


def deal_card():

    time.sleep(1)
    return deck.pop(random.randint(0, (len(deck)-1)))


def get_initial_cards():

    # two cards to player, two cards to dealer
    for _ in range(2):
        cards_dealt['player'].append(deal_card())
        cards_dealt['dealer'].append(deal_card())


def play():
    playing = True
    print(logo)
    print('Welcome to the Blackjack table!')
    while playing:
        clear()
        print("Let's deal them cards ...")
        # two cards to the player, two to the dealer
        get_initial_cards()
        print(f"Player has {display_hand('player')}")
        print(f"Dealer's first card is {cards_dealt['dealer'][0]}")
        # complete building player's hand, dealer wins if player busts
        if complete_hand('player') == 'dealer':
            print('The dealer wins')
        else:
            print(f"Player has {cards_dealt['player'][0]}, {cards_dealt['player'][1]}")
            # complete building dealer's hand automatically, checking to see who has
            # won
            winner = complete_hand('dealer')
            print(f'The winner is {winner}')
        print('Do you want to play again? (Y/n)')
        if (input('> ')).lower() != 'y':
            playing = False
        else:
            setup()
    else:
        print('Thank you for playing. Goodbye!')

play()