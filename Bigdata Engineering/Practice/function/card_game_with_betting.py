import simple_card_game2
import random

# define print_result function
def print_result(my_score, dealer_score):
    if my_score > dealer_score:
        result = "Win"
    elif my_score < dealer_score:
        result = "Lose"
    else:
        result = "Draw"
    print(result)
    return result

# define draw_a_card function
def draw_a_card(card_list):
    random_index = random.randint(0, len(card_list)-1)
    card = card_list.pop(random_index)
    return card

# define get_score function
def get_score(card_list, owner = "me"):
    card_sum = sum(card_list)
    print(card_list)
    print("score of %s: %d" %(owner, card_sum))
    return card_sum

# define play_a_round function
def play_a_round():
    cards = list(range(1, 12)) * 4
    my_cards, dealer_cards = [], []

    for i in range(2):
        my_cards.append(draw_a_card(cards))
        dealer_cards.append(draw_a_card(cards))

    my_sum = get_score(my_cards, 'me')
    dealer_sum = get_score(dealer_cards, 'dealer')

    return print_result(my_sum, dealer_sum)

# define play_with_betting
def play_with_betting(my_chips, dealer_chips):
    while my_chips > 0 and dealer_chips > 0 :
        print(f"my chips: {my_chips}, dealer chips: {dealer_chips}")
        my_betting = int(input(f"how much do you bet? (<={min(my_chips, dealer_chips)})"))
        round_result = play_a_round()

        if round_result == "Win":
            my_chips += my_betting
            dealer_chips -= my_betting
        elif round_result == "Lose":
            my_chips -= my_betting
            dealer_chips += my_betting

    return my_chips, dealer_chips

my_init, dealer_init = 100, 100
my_fin, dealer_fin = play_with_betting(my_init, dealer_init)

if my_fin == 0 :
    print("I lost all my chips")
else :
    print("Dealer lost all his/her chips")