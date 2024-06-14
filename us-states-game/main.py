import turtle
import answer_checker
import state_namer
from scoreboard import Scoreboard
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer_checker = answer_checker.State_checker()
scoreboard = Scoreboard()
state_namer = state_namer.StateNamer()
game_is_on = True

while(game_is_on):
    user_answer = screen.textinput(title=f"Your score: {scoreboard.get_score()}", prompt="What's another state's name?")
    user_answer = user_answer.lower()
    if user_answer == "exit":
        break
    if answer_checker.check_answer(user_answer):
        scoreboard.increment_score()
        state_data = answer_checker.get_xy(user_answer)
        state_namer.name_state(user_answer, int(state_data.x.iloc[0]),int(state_data.y.iloc[0]))
        screen.title(f"US state guesser")

# states_to_learn.csv
answer_checker.create_answer_csv()