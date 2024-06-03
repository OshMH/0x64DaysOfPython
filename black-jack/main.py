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
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn

import random

def get_rand():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
class Hand():
    def __init__(self):
        self.hand = [get_rand(),get_rand()]
    def hit(self):
        """"append a card from cards into the dealers or players hand"""
        self.hand.append(get_rand())
        
        if 11 in self.hand and sum(self.hand) > 21:
                        self.hand.remove(11)
                        self.hand.append(1)
    def restart(self):
        self.hand.clear()
        self.hand = [get_rand(),get_rand()]


class Game():
    dealer = Hand()
    player = Hand()
    def __init__(self):
        print("playing blaccckjack")
    def play(self):
        while(sum(self.player.hand) < 21 and sum(self.dealer.hand) <21):
            self.showPlayerCards()
            self.showDealerCard(1)
            answer = input("Type 'y' to get another card, type 'n' to pass: ")
            if answer =='y':
                self.player.hit()

            if answer =='n':
                while(sum(self.dealer.hand) < sum(self.player.hand) and sum(self.dealer.hand) < 17):
                    self.dealer.hit()
                break
        
        self.checkWinner()
    def showPlayerCards(self):
        print(f"Your cards: {self.player.hand}, current score: {sum(self.player.hand)}")
    def showDealerCard(self, *args):
        if args[0] ==1:
            print(f"Computer's first card: {self.dealer.hand[0]}")
        if args[0] == 2:
            print(f"Computer's hand: {self.dealer.hand}, current score: {sum(self.dealer.hand)}")
    def checkWinner(self):
        self.showPlayerCards()
        self.showDealerCard(2)
        if sum(self.player.hand) > 21:
            print("you busted!\nThe dealer wins!")
        elif sum(self.dealer.hand) > 21:
            print("you win!")
        elif sum(self.dealer.hand) > sum(self.player.hand):
            print("Dealer wins!")
        else:
            print("you win!")


def main():
    startGameAnswer = input("Do you want to play blackjack? type 'y' or 'n': ")
    continuePlaying = 'y'
    while(continuePlaying =='y' and startGameAnswer == 'y'):
        game = Game()
        game.play()
        continuePlaying = input("Do you want to play another game? ")
        if continuePlaying =='y':
            game.dealer.restart()
            game.player.restart()
            
        


if __name__=="__main__":
    main()

    
