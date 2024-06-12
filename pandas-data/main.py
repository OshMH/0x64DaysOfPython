import pandas
# with open("weather_data.csv") as weather_data:
#     weather_list = weather_data.readlines()


# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] !='temp':
#             temperatures.append(int(row[1]))


# data = pandas.read_csv('weather_data.csv')
# temp_list = data['temp'].to_list()

# average_temp = sum(temp_list)/len(temp_list)
# print(data['temp'].max())


# Get data in the rows 
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.temp[0])
# def F_to_C(temp):
#     return (temp*(9/5))+32
# print(F_to_C(monday.temp[0]))

# Create a dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# 230 The Great Squirrel Census Data Analysis (with Pandas)
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240613.csv")

primary_fur_color = data["Primary Fur Color"]

gray_fur = primary_fur_color[data['Primary Fur Color'] == "Gray"]
cinnamon_fur = primary_fur_color[data['Primary Fur Color'] == "Cinnamon"]
black_fur = primary_fur_color[data['Primary Fur Color'] == "Black"]

fur_color_data = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [len(gray_fur), len(cinnamon_fur), len(black_fur)]
}
pandas_fur_data = pandas.DataFrame(fur_color_data)
pandas_fur_data.to_csv("squirrel_count.csv")