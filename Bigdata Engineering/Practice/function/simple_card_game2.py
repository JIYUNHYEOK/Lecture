import random

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

# define print_result function
def print_result(my_score, dealer_score):
    if my_score > dealer_score:
        print("Win")
    elif my_score < dealer_score:
        print("Lose")
    else:
        print("Draw")


cards = list(range(1,12)) * 4
my_cards, dealer_cards = [], []

for i in range(2):
    my_cards.append(draw_a_card(cards))
    dealer_cards.append(draw_a_card(cards))

my_sum = get_score(my_cards, 'me')
dealer_sum = get_score(dealer_cards, 'dealer')

print_result(my_sum, dealer_sum)