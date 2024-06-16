import pandas
class State_checker():
    def __init__(self):
        self.correct_answers = []
        self.state_data = pandas.read_csv("50_states.csv")
        self.state_data['state'] = self.state_data['state'].apply(str.lower)
    
    def check_answer(self,user_answer):
        """Checks if the state is in the data, if it is,
            it will return the series of that data. If its
            not it will return false"""
        
        if user_answer in self.state_data.values:
            self.correct_answers.append(user_answer)
            return True
        
        return False
   
    def get_xy(self, user_answer):
        
        return self.state_data[self.state_data['state'] == user_answer]
    
    def create_answer_csv(self):
        for answer in self.correct_answers:
            self.state_data = self.state_data.drop(self.state_data[self.state_data['state'] == answer].index)
        self.state_data.to_csv("states_to_learn.csv")    
    
