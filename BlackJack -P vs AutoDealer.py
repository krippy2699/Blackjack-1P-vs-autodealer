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


# In[31]:


#Welcome and rule section
print('######## LETS PLAY SOME BLACKJACK ! ########')
print('RULES: \n->1.Table entry is at a minimum of $500 \n->2.No counting cards \n->3.The face value of an ACE is 11 \n->4.Winning hands make 1.5xbet \n->5.Player can request a hit only once \n->6.Bet is returned for when player and dealer play the same card  \n->7.GOOD LUCK !')
print('############################################')

#variables 
i = 0      #used as a counter
table_bet = 0
hit = False
stay = False
go_again = True
goagain_input = ' '
hit_or_stand = ''
#to display round number
hand = 1 
player_bet = 0 # the money user bets on his hand




#player information -------------------------------------------
print('\n         PLAYER INFORMATION             ')
name = input('Enter player name: ')
money = input('Enter betting money(>500$):')

while (money.isdigit() == False):
    print('Please enter a valid integer value')

while (float(money)<500):
    print(f'Only Players with $500 and above are allowed to play')
    money = input('Enter betting $: ')
#------------------------------------------------------------------
print('\n--------------------------------------------')
# Shufflingx2, Dealing and showing user their cards-------------------------------
    
    

#instantialting player objects - player and dealer
player = Player(name,int(money))
dealer_guy = Player('Dealer',0)
#dealing cards to the player
    
while go_again == True:
    print(f'               HAND #{hand}     ')
    print(f'----- you have ${player.tot_money} to play with -----')
    
    if player.tot_money <= 50:
        print('Sorry, your low on funds !')
        break
    
    
   #instantiation
    dealer = Dealer()
    #a fresh shuffle 
    dealer.shuffling()
    
    #dealing cards - player and dealer
    c1 = dealer.deal_one()
    player.add_cards(c1)
    c2 = dealer.deal_one()
    player.add_cards(c2)
    c3 = dealer.deal_one()
    dealer_guy.add_cards(c3)
    c4 = dealer.deal_one()
    dealer_guy.add_cards(c4)

    print(f'cards dealt ->  {player.hand[0]}({player.hand[0].intval}) \n\t\t{player.hand[1]}({player.hand[1].intval})')

#----------------------------------------------------------------------

    #user decides if they want to stay or not
    hit_or_stand = input("Enter s to 'Stay' and h to 'Hit': ")
    while hit_or_stand!='s' and hit_or_stand!='h' and hit_or_stand.lower()!='s' and hit_or_stand.lower()!='h':
        hit_or_stand = input('Enter either s or h: ')

    if hit_or_stand.lower()=='h' or hit_or_stand=='h':
        hit = True
    if hit_or_stand.lower()=='s' or hit_or_stand=='s':
        stay = True
    
#print('----------------------------------------------')
#----------------------------------------------------------------

    # If the player decides to stay
    if stay==True:
        player_bet = input('\nBet on your hand:$ ')

        #checking if bet is a digit
        while player_bet.isdigit()==False:
            print('Please enter integers')
            player_bet = input('Please enter a valid bet:$ ')

        #checking if bet is less than 0 or more than the player's starting betting money
        while int(player_bet) < 0 or int(player_bet) > player.tot_money: 
            print(f'Enter $ > 0 or $ < {player.tot_money}')
            player_bet = input('Please enter valid bet:$ ')

        player.tot_money = player.tot_money - int(player_bet)

        print('--------------------------------------')   

        if player.hand[0].intval + player.hand[1].intval <= 21:

            if player.hand[0].intval + player.hand[1].intval > dealer_guy.hand[0].intval + dealer_guy.hand[1].intval:
                print(f"-> WINNER WINNER CHICKEN DINNER !\n->The dealer's hand had {dealer_guy.hand[0]}({dealer_guy.hand[0].intval}) and {dealer_guy.hand[1]}({dealer_guy.hand[1].intval})")
                player.tot_money = player.tot_money + int(player_bet) + 0.5*int(player_bet)
                print(f'-> {player.name}, your betting money has now gone upto {player.tot_money}')
            
            elif player.hand[0].intval + player.hand[1].intvl == dealer_guy.hand[0].intval + dealer_guy.hand[1].intval:
                print(f"-> TIE ! BET was neither won nor lost !")
                print(f"-> The dealer had {dealer_guy.hand[0]} and {dealer_guy.hand[1]}")
                player.tot_money = player.tot_money + int(player_bet)
                print(f'-> {player.name}, your betting money is still {player.tot_money}')
                

            elif player.hand[0].intval + player.hand[1].intval < dealer_guy.hand[0].intval + dealer_guy.hand[1].intval:
                print(f'-> BETTER LUCK NEXT TIME !')
                print(f"-> The dealer's hand had {dealer_guy.hand[0]}({dealer_guy.hand[0].intval}) and {dealer_guy.hand[1]}({dealer_guy.hand[1].intval})")
                print(f'-> {player.name}, your betting money has now gone down to {player.tot_money}')

        else:

            print('BUST ! Your hand went over 21')
            print(f'{player.name},you now have {player.tot_money}')

 #--------------------------------------------------------------------------

    #if the player decides to hit - the dealer deals another card to the player and the player now bets on the hand against the dealer 
    if hit==True:

        hit_card = dealer.deal_one()
        player.add_cards(hit_card)

        print(f'Player hand after hit -> {player.hand[0]}({player.hand[0].intval}) \n\t\t\t {player.hand[1]}({player.hand[1].intval}) \n\t\t\t {player.hand[2]}({player.hand[2].intval})')

        player_bet = input('\nBet on your hand:$ ')

        #checking if bet is a digit
        while player_bet.isdigit()==False:
            print('Please enter integers')
            player_bet = input('Please enter a valid bet:$ ')

        #checking if bet is < 0 or > the player's starting betting money
        while int(player_bet) < 0 or int(player_bet) > player.tot_money: 
            print(f'Enter $ > 0 or $ < {player.tot_money}')
            player_bet = input('Please enter valid bet:$ ')

        player.tot_money = player.tot_money - int(player_bet)

        print('---------------------------------------------')    
        if player.hand[0].intval + player.hand[1].intval + player.hand[2].intval <= 21:
            
            
            if player.hand[0].intval + player.hand[1].intval + player.hand[2].intval > dealer_guy.hand[0].intval + dealer_guy.hand[1].intval:
                print(f"-> WINNER WINNER CHICKEN DINNER !\n->The dealer's hand had {dealer_guy.hand[0]}({dealer_guy.hand[0].intval}) and {dealer_guy.hand[1]}({dealer_guy.hand[1].intval})")
                player.tot_money = player.tot_money + int(player_bet) + 0.5*int(player_bet)
                print(f'-> {player.name}, your betting money is now {player.tot_money}')
            
            elif player.hand[0].intval + player.hand[1].intval + player.hand[2].intval == dealer_guy.hand[0].intval + dealer_guy.hand[1].intval:
                print(f"-> TIE ! BET was neither won nor lost !")
                print(f"-> The dealer had {dealer_guy.hand[0]} and {dealer_guy.hand[1]} and {dealer_guy.hand[2]}")
                player.tot_money = player.tot_money + int(player_bet)
                print(f'-> {player.name}, your betting money is still {player.tot_money}')
                

            elif player.hand[0].intval + player.hand[1].intval + player.hand[2].intval < dealer_guy.hand[0].intval + dealer_guy.hand[1].intval:
                print(f'-> BETTER LUCK NEXT TIME !')
                print(f"-> The dealer's hand won with {dealer_guy.hand[0]}({dealer_guy.hand[0].intval}) and {dealer_guy.hand[1]}({dealer_guy.hand[1].intval})")
                print(f'-> {player.name}, you now have {player.tot_money} to play with')

        else:

            print('BUST ! Your hand went over 21')
            print(f'-> {player.name},you now have {player.tot_money}')

    #--------------------------------------------------------------------
    
    hand += 1
    stay = False
    hit = False
    #emptying dealer and players hands
    player.hand.clear()
    dealer_guy.hand.clear()
    
    goagain_input = input('Enter y(YES) to continue or n(NO) to quit: ')  
    while goagain_input!='y' and goagain_input!='n' and goagain_input.Lower()!='y' and goagain_input.Lower()!='n':
        goagain_input = input('Enter either y or n: ')

    if goagain_input=='y' or goagain_input.lower()=='y':
        go_again = True
    elif goagain_input=='n' or goagain_input.lower()=='n':
        go_again = False
    print('-----------------------------------------')

#exit message    
print('#######################################')
print(f"TODAY YOU'LL BE LEAVING WITH {player.tot_money}")
print('I HOPE YOU HAD FUN!')
print('#######################################')    

    
    


# In[26]:





# In[27]:





# In[ ]:




