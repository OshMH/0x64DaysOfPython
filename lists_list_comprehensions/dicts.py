
# Format for dictonary comprehensions are:
# new_dict ={new_key:new_value for item in list}

# Format for creating dictionaries from other dictionaries with comprehensions are:
# new_dict ={new_key:new_value for (key,value) in dict.items()}
from random import randint
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

student_scores = {name:randint(0,100) for name in names}

# print(student_scores)

# Loop through a dict

passed_students = {student:score for (student,score) in student_scores.items() if score > 49}

# print(passed_students)

#Looping through rows of a data frame
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
for (index, row) in  student_data_frame.iterrows():
    print(row)

