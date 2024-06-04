import game_data
import art
import random
class HighLow():
    data = game_data.data
    def __init__(self):
        print(art.logo)
        self.stop = False
        self.score = 0
    def startGame(self):
        a = random.choice(self.data)
        b = random.choice(self.data)
        if a.get('name') == b.get('name'):
            b = random.choice(self.data)
        
        while(not self.stop):
            print(f"Compare A: {a.get('name')}, a {a.get('description')}, from {a.get('country')}")
            print(art.vs)
            print(f"Compare B: {b.get('name')}, a {b.get('description')}, from {b.get('country')}")
            correctAnswer = 'A' if a.get('follower_count') > b.get('follower_count') else 'B'
            if input("Who has more followers? Type 'A' or 'B': ").upper() == correctAnswer:
                self.score += 1
                print(f"You're right! Current score: {self.score}")
            else:
                print(f"Sorry, that's wrong. Final score: {self.score}")
                self.stop = True

            a = b
            b = random.choice(self.data)

        



def main():
    hl = HighLow()
    hl.startGame()
if __name__=="__main__":
    main()


