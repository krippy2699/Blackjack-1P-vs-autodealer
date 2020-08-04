#!/usr/bin/env python
# coding: utf-8

# In[1]:


ranks = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
suits = ['Clubs','Spades','Diamond','Hearts']
value = {'Ace':11,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}


# In[2]:


class card:
    
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.intval = value[rank]
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'


# In[3]:


from random import shuffle

class Dealer:
    
    def __init__(self):
        self.deck = []
        
        for sui in suits:
            for ran in ranks:
                building_card = card(ran,sui)
                self.deck.append(building_card)
    
    def shuffling(self):
        return shuffle(self.deck)
    
    # while dealing we're popping the top most card because if you think about it,
    # the dealer deals from the top and not the bottom 
    def deal_one(self):
        return self.deck.pop()
                


# In[4]:


class Player:
    
    
    def __init__(self,name,tot_money):
        self.name = name
        self.tot_money = tot_money 
        self.hand = []
    
    #for when you dealing cards to a player
    def add_cards(self,new_card):
        self.hand.append(new_card)
    
    def __str__(self):
        return f'{self.name} has {len(self.hand)} cards. '


# In[5]:


def get_player():
    
    player_money = 0
    player_name = input('Enter player name: ')
    player_money = input('Enter betting money(<$500):$ ')
    
    while player_money.isdigit()!=True or int(player_money)<500:
        print('Please enter a valid integer input(>$0):$ ')
        player_money = input('Enter bet:$ ')
        
    player = Player(player_name,int(player_money))
    
    return player
    


# In[6]:


def hit_or_stay():
    
    user_input = input('Enter h(to HIT) or s(to STAY):')
    
    while user_input!='h' and user_input!='s' and user_input.lower()!='h' and user_input.lower()!='s':
        user_input = input('Enter either h or s: ')
        
    return user_input


# In[7]:


def bet(player_mon):
    
    user_input = input(f'Enter bet (You have ${player_mon}):$ ')
    
    while user_input.isdigit() == False or int(user_input)<0 or int(user_input)>player_mon:
        print('!! Enter valid input please !!')
        user_input = input(f'Enter between 0 and {player_mon}:$ ')
    
    return user_input


# In[8]:


def quit_or_continue():
    
    user_input = input('Continue betting? y(YES) or n(NO): ')
    
    while user_input!='y' and user_input!='n' and user_input.lower()!='y' and user_input.lower()!='n':
        print('!! Enter valid input please !!')
        user_input = input('Enter either y or n: ')
                           
    return user_input


# In[9]:


def stay(player,dealer_emp,player_bet):
    
    player.tot_money = player.tot_money - int(player_bet)
    
    if player.hand[0].intval + player.hand[1].intval <= 21:

            if player.hand[0].intval + player.hand[1].intval > dealer_emp.hand[0].intval + dealer_emp.hand[1].intval:
                print(f"-> WINNER WINNER CHICKEN DINNER !\n->The dealer's hand had {dealer_emp.hand[0]}({dealer_emp.hand[0].intval}) and {dealer_emp.hand[1]}({dealer_emp.hand[1].intval})")
                player.tot_money = player.tot_money + int(player_bet) + 0.5*int(player_bet)
                print(f'-> Betting money has now gone upto ${player.tot_money}')
            
            elif player.hand[0].intval + player.hand[1].intval == dealer_emp.hand[0].intval + dealer_emp.hand[1].intval:
                print(f"-> TIE ! BET was neither won nor lost !")
                print(f"-> The dealer had {dealer_emp.hand[0]} and {dealer_emp.hand[1]}")
                player.tot_money = player.tot_money + int(player_bet)
                print(f'-> Betting money is still ${player.tot_money}')
                

            elif player.hand[0].intval + player.hand[1].intval < dealer_emp.hand[0].intval + dealer_emp.hand[1].intval:
                print(f'-> BETTER LUCK NEXT TIME !')
                print(f"-> The dealer's hand had {dealer_emp.hand[0]}({dealer_emp.hand[0].intval}) and {dealer_emp.hand[1]}({dealer_emp.hand[1].intval})")
                print(f'-> Betting money has now gone down to ${player.tot_money}')

    elif player.hand[0].intval + player.hand[1].intval > 21:
        print('BUST ! Your hand went over 21')
        print(f'{player.name},you now have ${player.tot_money}')
    
    return player.tot_money
    


# In[10]:


def hit(player,dealer_emp,curr_deck):
    
    hit_card = curr_deck.deal_one()
    player.add_cards(hit_card)
    
    print(f'hand after hitting ->  {player.hand[0]}({player.hand[0].intval}) \n\t\t{player.hand[1]}({player.hand[1].intval}) \n\t\t{player.hand[2]}({player.hand[2].intval})')
    
    player_bet = bet(player.tot_money)
    
    player.tot_money = player.tot_money - int(player_bet)
    
    if player.hand[0].intval + player.hand[1].intval + player.hand[2].intval <= 21:
            
            
            if player.hand[0].intval + player.hand[1].intval + player.hand[2].intval > dealer_emp.hand[0].intval + dealer_emp.hand[1].intval:
                print(f"-> WINNER WINNER CHICKEN DINNER !\n->The dealer's hand had {dealer_emp.hand[0]}({dealer_emp.hand[0].intval}) and {dealer_emp.hand[1]}({dealer_emp.hand[1].intval})")
                player.tot_money = player.tot_money + int(player_bet) + 0.5*int(player_bet)
                print(f'-> Betting money has gone upto ${player.tot_money}')
            
            elif player.hand[0].intval + player.hand[1].intval + player.hand[2].intval == dealer_emp.hand[0].intval + dealer_emp.hand[1].intval:
                print(f"-> TIE ! BET was neither won nor lost !")
                print(f"-> The dealer had {dealer_emp.hand[0]} and {dealer_emp.hand[1]} and {dealer_emp.hand[2]}")
                player.tot_money = player.tot_money + int(player_bet)
                print(f'-> Betting money is still ${player.tot_money}')
                

            elif player.hand[0].intval + player.hand[1].intval + player.hand[2].intval < dealer_emp.hand[0].intval + dealer_emp.hand[1].intval:
                print(f'-> BETTER LUCK NEXT TIME !')
                print(f"-> The dealer's hand won with {dealer_emp.hand[0]}({dealer_emp.hand[0].intval}) and {dealer_emp.hand[1]}({dealer_emp.hand[1].intval})")
                print(f'-> Betting has gone down to ${player.tot_money}')

    elif player.hand[0].intval + player.hand[1].intval + player.hand[2].intval > 21:

                print('BUST ! Your hand went over 21')
                print(f'-> {player.name},you now have ${player.tot_money}')
    
    return player.tot_money
    


# In[13]:


#local variable
hand = 1
continuing = False

#Welcome and rules bit
print('################## LETS PLAY SOME BLACKJACK ! #################')
print('RULES: \n->1.Table entry is at a minimum of $500 \n->2.No counting cards \n->3.The face value of an ACE is 11 \n->4.Winning hands make 1.5xbet \n->5.Player can request a hit only once \n->6.Bet returned for when player and dealer play the same hand  \n->7.GOOD LUCK !')
print('################################################################')


print('\n-------------------- PLAYER INFORMATION ----------------------')
player = get_player()
dealerr = Player('Dealer',0)

while continuing==False:
    
    if player.tot_money == 0:
        print('Insufficient funds !')
        break
    
    deckk = Dealer()
    
    deckk.shuffling()
    
    card1 = deckk.deal_one()
    player.add_cards(card1)
    card2 = deckk.deal_one()
    player.add_cards(card2)
    card3 = deckk.deal_one()
    dealerr.add_cards(card3)
    card4 = deckk.deal_one()
    dealerr.add_cards(card4)
    
    print('-------------------------------------------------------------')
    print(f'\n                    HAND#{hand}                       ')
    print(f'Player hand ->  {player.hand[0]}({player.hand[0].intval})\n\t\t{player.hand[1]}({player.hand[1].intval})')
    
    hors_input = hit_or_stay()
    if hors_input == 's':
        print('-------------------------------')
        player_bet = bet(player.tot_money)
        player.tot_money = stay(player,dealerr,player_bet)
          
    elif hors_input == 'h':
        print('-------------------------------')
        hit(player,dealerr,deckk)
        
    print('-------------------------------------------------------------')
    continue_input = quit_or_continue()
    if continue_input == 'y':
        coninuing = False
    elif continue_input == 'n':
        continuing = True

    player.hand.clear()
    dealerr.hand.clear()
    deckk.deck.clear()
    hand+=1

print('\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print(f'Your proceedings from todays come down to ${player.tot_money}')
print('Thank you for playing !')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




