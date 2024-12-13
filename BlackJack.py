import random

card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
dealer_cards = []
current_cards = []
card_sum = 0


for i in range(2):
    ran_card = random.randint(0,len(card_list)-1)
    current_cards.append(card_list[ran_card])
    dealer_card = random.randint(0,len(card_list)-1)
    dealer_cards.append(card_list[dealer_card])      

def dealer_calc():
    deal_sum = 0
    for index in range(2):
        deal_sum += dealer_cards[index]
        index += 1
    return deal_sum



def add_cards():
    ran_extra_card = random.randint(0,len(card_list)-1)
    current_cards.extend([card_list[ran_extra_card]])
    

def card_calc():
    player_sum = card_sum
    for index in range(len(current_cards)):
        player_sum += current_cards[index]
    return player_sum
    
    
    

while True:
    dealcard_sum = dealer_calc()
    calc = card_calc()
    ask = input('Your cards are: ' + str(current_cards) + '\nYour Total: ' + str(calc) + '\nHit or Stay?')
    if ask == 'Hit':
        add_cards()
        calc
    elif ask == 'Stay':
        if card_sum > 21:
            print('Dealer Cards:' + str(dealer_cards))
            print('Dealer Total: ' + str(dealcard_sum))
            print('You Lose')
            break
        dealcard_sum
        if calc == 21 or (calc < 21 and calc > dealcard_sum) or dealcard_sum > 21:
            print('Dealer Cards:' + str(dealer_cards))
            print('Dealer Total: ' + str(dealcard_sum))
            print('You Win')
            break
        elif calc == dealcard_sum:
            print('Dealer Cards:' + str(dealer_cards))
            print('Dealer Total: ' + str(dealcard_sum))
            print('TIE')
            break
        else:
            print('Dealer Cards:' + str(dealer_cards))
            print('Dealer Total: ' + str(dealcard_sum))
            print('You Lose')
            break
    
    else:
        pass