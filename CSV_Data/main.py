# f = open("../../PycharmProjects/CSV_Data/weather_data - S.csv", "r")
# new_f = f.readlines()
# print(new_f)

# To work with the code we need to extract the data, using the help of an inbuilt library, first import the CSV library.

# import csv
#
# with open("weather_data - S.csv") as data_file:

# reader is a csv method, which takes the file in question, and it reads and output the data.

# data = csv.reader(data_file)
# temperatures = []
# for row in data:
#
# What it has done is that it has taken each of the rows inside our weather_data.csv,
# and separated out each item into a single value.
#
# print(row)
#     if len(row[1]) <= 2 or row[1] != "temp":
#         temperatures.append(int(row[1]))
# print(temperatures)
#
# But there is an easier way to go about analyzing this data with the use of Pandas library.
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# sum_no = 0
# for nos in temp_list:
# sum_no += nos
# print(f"Average = {sum_no//len(temp_list)}")
# or we can sort this out using one of the series method
# print(data["temp"].mean())
# print(data["temp"].max())
#
# Get Data in Row
# print(data[data.day == "Monday"])
#
# Print the row of data which had the highest temperature.
# maximum = data["temp"].max()
# print(data[data.temp == maximum])
# or we use angela's approach
# print(data[data.temp == data.temp.max()])
#
# There are different ways to call
# data["temp"]
# or as an attribute
# data.temp
#
# Convert Monday's temperature to Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(f"Temperature in Fahrenheit = {monday_temp_F}")
#
# Create a dataframe from scratch
# data_dict = {
#     "students": ["Away", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
#
# # To create a csv file for the data
# data.to_csv("new_data.csv")
#
# Goal: Create a CSV called squirrel_count, that has a small table which contains the fur color and list the no of
# color, based on the primary fur color.
#
# Eg:
# ,Fur Color, Count
# 0,grey,2473
# 1,cinnamon,392
# 2,black,103
#
# squirrel_color = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231231.csv")
# color_list = squirrel_color["Primary Fur Color"].to_list()
# no_of_Gray = []
# no_of_Black = []
# no_of_Cinnamon = []
# for fur_color in color_list:
#     if fur_color == "Gray":
#         no_of_Gray.append(fur_color)
#     elif fur_color == "Black":
#         no_of_Black.append(fur_color)
#     elif fur_color == "Cinnamon":
#         no_of_Cinnamon.append(fur_color)
#
# primary_fur_color = {
#     "Fur Color": ["Cinnamon", "Gray", "Black"],
#     "Count": [len(no_of_Cinnamon), len(no_of_Gray), len(no_of_Black)]
# }
# squirrel_fur_color = pandas.DataFrame(primary_fur_color)
# squirrel_fur_color.to_csv("squirrel_count.csv")
# I know Angela will have a shorter approach to all this jargon code that i have written here.
#
Angela's code
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231231.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
