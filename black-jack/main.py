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
        answer = input("Type 'y' to get another card, type 'n' to pass:")
        if answer =='y':
            pass
    def showPlayerCards(self):
        print(f"Your cards: {self.player.hand}, current score: {sum(self.player.hand)}")
    def showDealerCard(self):
        print(f"Computer's first card: {self.dealer.hand[0]}")
            



def main():
    startGameAnswer = input("Do you want to play blackjack? type 'y' or 'n': ")
    if startGameAnswer == 'y':
        game = Game()
        game.play()


if __name__=="__main__":
    main()

# hand = Hand()
# hand.hit()
# hand.stand()
# print(hand.stand)
# print(hand.hand)
# print(sum(hand.hand))

    
