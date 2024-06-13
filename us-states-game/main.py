import turtle
import pandas
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
    user_answer = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    if answer_checker.check_answer(user_answer):
        scoreboard.increment_score()
        state_data = answer_checker.get_xy(user_answer)
        state_namer.name_state(user_answer, int(state_data.x),int(state_data.y))



turtle.mainloop()