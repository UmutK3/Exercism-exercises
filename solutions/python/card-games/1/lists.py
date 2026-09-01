def get_rounds(number):
    number_list = []
    number_list2 = [number,number + 1,number + 2]
    number_list.extend(number_list2)
    return number_list

def concatenate_rounds(rounds_1 , rounds_2):
    rounds_1.extend(rounds_2)
    return rounds_1

def list_contains_round(rounds, number):
    return True if number in rounds else False
        
def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    middle_card = hand[len(hand) // 2 ]
    average_first_last = (hand[0] + hand[-1]) / 2
    return True if card_average(hand) == middle_card or card_average(hand) == average_first_last else False
print(approx_average_is_average([2, 3, 4, 8, 8]))
            
def average_even_is_average_odd(hand):
    odd_cards = []
    even_cards = []
    for card in hand:
        if card % 2 == 0:
            even_cards.append(card)
        else:
            odd_cards.append(card)
    if odd_cards == [] or even_cards == []:
        return True
    return True if card_average(odd_cards) == card_average(even_cards) else False
            
def maybe_double_last(hand):
    last_card = hand[-1]
    if last_card == 11:
        hand[-1] = last_card * 2
    return hand

