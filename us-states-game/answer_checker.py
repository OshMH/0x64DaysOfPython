import pandas


class State_checker():

    def __init__(self):
        self.correct_answers = []
        self.state_data = pandas.read_csv("50_states.csv")
    
    def check_answer(self,user_answer):
        """Checks if the state is in the data, if it is,
            it will return the series of that data. If its
            not it will return false"""
        
        return user_answer in self.state_data.values
    def get_xy(self, user_answer):
        return self.state_data[self.state_data['state'] == user_answer]

    
