def value_of_card(card):
    if card == "J" or card == "K" or card == "Q":
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return card_one, card_two
    
def value_of_ace(card_one, card_two):
    if card_one == "A" or card_two == "A"
    elif value_of_card(card_one) + value_of_card(card_two) + 11 <= 21:
        return 11
    elif value_of_card(card_one) + value_of_card(card_two) + 11 > 21:
        return 1
    

def is_blackjack(card_one, card_two):
    if card_one == "A" and card_two == "A":
        return False
    elif (value_of_card(card_one) == 10 or value_of_card(card_two) == 10) and  card_one == "A" or card_two == "A":
        return True
    else:
        return False
print(is_blackjack("10","2"))
def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False

def can_double_down(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two) ==  (9 or 10 or 11):
        return True
    else:
        return False
