
from copy import deepcopy


def add_cards(deck, card1, card2):
    return deck.extend([card1, card2])

def create_decks(contents):
    tmp = list()
    for line in contents:
        if line.isdigit():
            tmp.append(int(line))
        elif not line:
            deck1 = tmp
            tmp = list()
    
    return deck1, tmp


def draw_card(deck):
    # pop top card, return card plus remaining deck
    draw = deck.pop(0)
    return draw, deck


def calcluate_score(deck):
    multiplier = len(deck)
    total = 0
    for card in deck:
        total += card * multiplier
        multiplier -= 1
    
    return total


def recursive_combat(deck1, deck2):
    # print(f'----Starting a new game----')
    # print(f'Deck 1: {deck1}')
    # print(f'Deck 2: {deck2}')

    p1_deck_hist = list()
    p2_deck_hist = list()

    while len(deck1) > 0 and len(deck2) > 0:

        if deck1 in p1_deck_hist or deck2 in p2_deck_hist:
            print(f'***Player 1 wins because of repeat***')
            return "p1", calcluate_score(deck1)
        else:
            p1_deck_hist.append(deepcopy(deck1))
            p2_deck_hist.append(deepcopy(deck2))


        p1, deck1 = draw_card(deck1)
        p2, deck2 = draw_card(deck2)
        
        if p1 <= len(deck1) and p2 <= len(deck2):
            print(f'--Playing a subgame with {p1} and {p2}--')
            winner, _ = recursive_combat(deck1[:p1], deck2[:p2])
            if winner == 'p1':
                add_cards(deck1, p1, p2)
            elif winner == 'p2':
                add_cards(deck2, p2, p1)
            else:
                raise "recursive winner"
        elif p1 > p2:
            add_cards(deck1, p1, p2)
        elif p2 > p1:
            add_cards(deck2, p2, p1)
        else:
            raise "p1 and p2 are equal!"

    if len(deck1) == 0:
        print("*** Player 2 wins***")
        return "p2", calcluate_score(deck2)
    else:
        print("*** Player 1 wins***")
        return "p1", calcluate_score(deck1)


if __name__ == "__main__":
    with open('day22.txt') as fin:
        contents = [line.strip() for line in fin.readlines()]

    deck1, deck2 = create_decks(contents)

    winner, winner_score = recursive_combat(deck1, deck2)
    print(f'The winner is {winner} with {winner_score}')
