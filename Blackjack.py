#  File: Blackjack.py
#  Description: Simulate a game of blackjack between dealer and 1 player
#  Student's Name: Weiyi Wang
#  Student's UT EID: ww6874
#  Course Name: CS 313E 
#  Unique Number: 87530
#
#  Date Created: 6/21/2016
#  Date Last Modified: 6/29/2016


from random import shuffle

# Object card has two attributes, suit and pip
class Card:

    def __init__(self,pip,suit):
        self.suit = suit
        self.pip = pip
        
        if pip in ['2','3','4','5','6','7','8','9','10']:

            # If the pip is a number, then the value of the card = that number
            self.value = eval(pip)
            
        elif pip == 'J' or pip == 'Q' or pip == 'K':

            # Jack, Queen, King have value 10
            self.value = 10
            
        else:

            # Default value for ace will be 11. Will get modified later.
            self.value = 11

    def __str__(self):
        return(self.pip+self.suit)


# Object deck has 52 cards, each of different suit and pip
class Deck:


    def __init__(self):
        suitList = ['S','C','D','H']
        pipList = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.cardList = []


        # Go through the suits
        for suit in suitList:

            # Go through the pips
            for pip in pipList:

                # Add the cards of each suit and pip into the list
                self.cardList.append(Card(pip,suit))

    def __str__(self):
        
        strCardList = ''
        counter = 0
        for card in self.cardList:
            counter = counter + 1
            if counter == 13:
                strCardList = strCardList + str(card) +'\n'
                counter = 0
            else:
                strCardList = strCardList + str(card) + '  '

        return strCardList
    
    def shuffle(self):
        shuffle(self.cardList)

    def dealOne(self,person):

        person.hand.append(self.cardList[0])
        del self.cardList[0]


class Player(Deck):


    # Make a hand of cards
    def __init__(self):
        self.hand = []
        
        

    def __str__(self):

        strHand = ''
        for card in self.hand:
            strHand = strHand + str(card) + '  '
        
        return strHand



def showHands(player,dealer):

    print('You hold',player,'for a total of',calcHand(player))
    print('Dealer has',dealer.hand[0],'and one facedown card')
            

# Find the hand value of the player specified
def calcHand(player):
    points = 0

    # count the number of aces in the hand
    aces = 0
    
    for card in player.hand:


        # If the card is an ace, then add it to the count of aces
        if card.pip == 'A':
            aces = aces + 1
            
            
        
        points = points + card.value

        # If the points total > 21, check for aces
        if points > 21 and aces!=0:

            # If there exists an ace,
            # then change the value to 1, which decreases the points by 10
            
            points = points - 10

            # Use up one of the possible ace reductions
            aces = aces - 1

    return points
        

# Carry out a player's turn
def playerTurn(cardDeck,dealer,player):

    # If the condition blackjack is met, then end the loop
    blackjack = False


    # First I have to take care of the original hand

    # Store the points that the player has in original hand
    points = 0

    # count the number of aces in the hand
    aces = 0
    
    for card in player.hand:


        # If the card is an ace, then add it to the count of aces
        if card.pip == 'A':
            aces = aces + 1
            
            
        points = points + card.value
        

        # If the points total > 21, check for aces
        if points > 21 and aces!=0:

            print('Assuming 11 points for an ace in your hand for now')
            # If there exists an ace,
            # then change the value to 1, which decreases the points by 10
            print('Over 21. Reducing value of ace in your hand')
            points = points - 10
            print()
            
            # Use up one of the possible ace reductions
            aces = aces - 1
            


    # Show the player's hand and the dealer's hand
    print('You have',player.hand[0],player.hand[1],'for a total of',points)
    
    # If the starting hand contains an ace say so
    # and say its default value is 11
    if player.hand[0].pip == 'A' or player.hand[1].pip == 'A':
        print('Assuming 11 points for an ace in your hand for now')
        print()


    
    print('Dealer has',dealer.hand[0],'and one facedown card')
    print()
    
    
    
    if player.hand[0].value+player.hand[1].value==21:
        print('Blackjack')
        print('Your turn is over')
        print()
        blackjack = True

    
##    # Ask whether to hit or stay
##    # Conditions for terminating loop
##      # User wants to stay
##      # blackjack
##      # User busts
##
##
##
    while (not blackjack and points<21):
        hit_or_stay = input('1 (hit) or 2 (stay)? ')
        print()

        
        
        # If player chooses to hit, then deal card to player
        if hit_or_stay == '1':

            # The card dealt always comes from the top of the deck
            print('Card dealt:  ',cardDeck.cardList[0])

            
                
            cardDeck.dealOne(player)
            
            # If an ace is dealt
            if player.hand[-1].pip == 'A':

                # First assume that the ace is 11
                print('Assume the ace dealt is 11')
                points = points + 11
                # Add the ace dealt to the count of aces
                aces = aces + 1
                

                # If adding 11 points would bust
                if points> 21:

                    # Reduce the value of the ace dealt to 1
                    print('Over 21. Reducing ace value')
                    points = points - 10

                    # Use up one of the possible ace reductions
                    aces = aces - 1
                    

                # If adding 11 points wouldn't bust
                else:

                    # Keep the value of the aces as 11
                    points = points + 11

            # If the card dealt is not an ace
            else:

                # The card dealt puts points over 21
                if points + player.hand[-1].value > 21:

                    # If there is an ace, we can reduce its value
                    if aces > 0:
                        print('Over 21. Reduce previous ace value to 1')
                        points = points + player.hand[-1].value - 10
                        aces = aces - 1
                        

                    # If there is no ace, just let them bust
                    else:
                        points = points + player.hand[-1].value
                        

                # If the card dealt doesn't bust
                else:
                    points = points + player.hand[-1].value
    
            
                
            print('New total: ',points)
            print()
            

        else:

            
            break

        # Check if 21, or bust and print appropriate message
        if calcHand(player) == 21:
            print('You have 21')
            print('Your turn is over')
            print()
            blackjack = True

        elif points > 21:
            print('Bust, dealer wins')
            
        
# Carry out a dealer's turn.
# Assume player's turn has already been carried out
def dealerTurn(cardDeck,dealer,player):

    print('Your Hand: ',end = '')
    for card in player.hand:
        print(card,end = ' ')
    print('for a total of',calcHand(player))
    
    print("Dealer's Hand:",dealer.hand[0],dealer.hand[1],'for a total of',calcHand(dealer))
    print()

    # First I have to take care of the original hand

    # Store the points that the player has in original hand
    points = 0

    # count the number of aces in the hand
    aces = 0
    
    for card in dealer.hand:


        # If the card is an ace, then add it to the count of aces
        if card.pip == 'A':
            aces = aces + 1
            
            
        points = points + card.value
        

        # If the points total > 21, check for aces
        if points > 21 and aces!=0:
            # In order for points in starting hand > 21, there must be two aces
            print("Assuming 11 points for an ace in dealer's hand for now")
            
            # Then change the value to 1, which decreases the points by 10
            print('Over 21. Reducing value of ace in hand')
            points = points - 10
            print('New total:',points)
            print()
            
            # Use up one of the possible ace reductions
            aces = aces - 1


    # Dealer has to keep hitting until he matches or beats the player's score
    while calcHand(dealer)<calcHand(player):
        print('Dealer hits:',cardDeck.cardList[0])
        cardDeck.dealOne(dealer)

        # If an ace is dealt
        if dealer.hand[-1].pip == 'A':

            # First assume that the ace is 11
            print('Assume the ace dealt is 11')
            points = points + 11
            # Add the ace dealt to the count of aces
            aces = aces + 1
                

            # If adding 11 points would bust
            if points> 21:

                # Reduce the value of the ace dealt to 1
                print('Over 21. Reducing ace value')
                points = points - 10
                
                # Use up one of the possible ace reductions
                aces = aces - 1
                    

            # If adding 11 points wouldn't bust
            else:

                # Keep the value of the aces as 11
                points = points + 11

        # If the card dealt is not an ace
        else:

            # The card dealt puts points over 21
            if points + dealer.hand[-1].value > 21:

                # If there is an ace, we can reduce its value
                if aces > 0:
                    print('Over 21. Reduce previous ace value to 1')
                    points = points + dealer.hand[-1].value - 10
                    aces = aces - 1
                        

                # If there is no ace, just let them bust
                else:
                    points = points + dealer.hand[-1].value
                        

            # If the card dealt doesn't bust
            else:
                points = points + dealer.hand[-1].value



        print('New Total:',calcHand(dealer))
        print()

    if calcHand(dealer)>21:
        print('Dealer has ',calcHand(dealer),'. Dealer busts! You win.',sep='')
    elif calcHand(dealer)<calcHand(player):
        print('Dealer has ',calcHand(dealer),'. Dealer has fewer points. You win.',sep='')
    elif calcHand(dealer)==calcHand(player):
        print('Dealer has ',calcHand(dealer),'. Dealer has same points. Dealer wins.',sep='')
    else:
        print('Dealer has ',calcHand(dealer),'. Dealer has more points. Dealer wins.',sep='')
        
    


def main():

    print('Initial deck:')
    newDeck = Deck()
    print(newDeck)


    print('Shuffled deck:')
    newDeck.shuffle()
    print(newDeck)


    print('Deck after dealing two cards each:')
    player1 = Player()
    dealer = Player()
    newDeck.dealOne(player1)
    newDeck.dealOne(dealer)
    newDeck.dealOne(player1)
    newDeck.dealOne(dealer)
    print(newDeck)
    print()

    
    showHands(player1,dealer)

    print()
    print('You go first')
    print()

    playerTurn(newDeck,dealer,player1)


    # If player already busted, dealer doesn't need to have a turn
    if calcHand(player1)>21:
        pass
    else:
        print("Dealer's turn")
        print()

        dealerTurn(newDeck,dealer,player1)

    print()
    print('Game Over')
    

main()
    
    
