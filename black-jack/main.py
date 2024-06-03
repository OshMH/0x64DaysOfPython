# if we go over 21, then we lose

# 2 to 10, its the face value
# Jack, Queen and King are 10
# Ace can be either 1 or 11

################### blackjack house rules ########################

## The deck is unlimited in size
## There are no jokers
## The Jack/Queen/King all count as 10
## the Ace can count as 11 or 1
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn

import random

def get_rand():
    return cards[random.randint(0, len(cards)-1)]
class Hand():
    hand:list = []
    stand:bool = False
    def __init__(self):
        self.hand = [get_rand(),get_rand()]
    def hit(self):
        self.hand.append(get_rand())
    def stand(self):
        self.stand = True
    def restart(self):
        self.hand.clear()
        self.__init__()


class Game():
    dealer = Hand()
    player = Hand()
    def __init__(self):
        print(f"playing blaccckjack\n your cards: {self.player.hand}, current score: {sum(self.player.hand)}\n Dealer's first card: {self.dealer.hand[0]}")
    def play(self):
        while(sum(self.player.hand) < 21 and sum(self.dealer.hand) <21):
            answer = input("Type 'y' to get another card, type 'n' to pass: ")
            if answer =='y':
                self.player.hit()
            if answer =='n':
                while(sum(self.dealer.hand) < sum(self.player.hand) and sum(self.dealer.hand) < 17):
                    self.dealer.hit()
            self.checkWinner()
            break
        
                
                
            
    def showPlayerCards(self):
        print(f"Your cards: {self.player.hand}, current score: {sum(self.player.hand)}")
    def showDealerCard(self, *args):
        if args[0] ==1:
            print(f"Computer's first card: {self.dealer.hand[0]}")
        if args[0] == 2:
            print(f"Computer's hand: {self.dealer.hand}, current score: {sum(self.dealer.hand)}")
    def checkWinner(self):
        if sum(self.player.hand) > 21:
            self.showPlayerCards()
            self.showDealerCard(2)
            print("you busted!\n The dealer wins!")
        elif sum(self.dealer.hand) > 21:
            self.showPlayerCards()
            self.showDealerCard(2)
            print("you win!")
        elif sum(self.dealer.hand) > sum(self.player.hand):
            self.showPlayerCards()
            self.showDealerCard(2)
            print("Dealer wins!")
        else:
            self.showPlayerCards()
            self.showDealerCard(2)
            print("you win!")




def main():
    startGameAnswer = input("Do you want to play blackjack? type 'y' or 'n': ")
    continuePlaying = 'y'
    while(continuePlaying =='y' and startGameAnswer == 'y'):
        game = Game()
        game.play()
        continuePlaying = input("Do you want to play another game?")
            
        


if __name__=="__main__":
    main()

    
