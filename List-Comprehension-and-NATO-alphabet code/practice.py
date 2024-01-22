# List Comprehension

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(numbers)
# [1, 2, 3]
# print(new_numbers)
# [2, 3, 4]

# name = "Angela"
# new_list = [letter for letter in name]

# digit = [no for no in range(1,5)]
# new_digit = [no * 2 for no in range(1, 5)]

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# names
# ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']
# names
# ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) < 5]
# longer_upperCap_names = [uppercase.upper() for uppercase in names if len(uppercase) > 4]

# squaring numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [squared**2 for squared in numbers]
# print(squared_numbers)

# Even numbers
# even_number = [even for even in numbers if even % 2 == 0]


# Data Overlap

# file1_list = []
# with open("file1.txt", "r") as file1:
#     data = file1.readlines()
#     file_data_1 = [file1_list.append(digit_1.strip("\n")) for digit_1 in data]
#
# with open("file2.txt", "r") as file2:
#     data = file2.readlines()
#     file_data_2 = [file1_list.append(digit_2.strip("\n")) for digit_2 in data]
#
# result = [final_data for final_data in file1_list if file1_list.count(final_data) > 1]
# print(result)
# import random
# Dictionary Comprehension
# students_scores = {student: random.randint(1, 100) for student in names}
# passed_students = {passed for passed in students_scores if students_scores[passed] > 60}
# passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
# print(students_scores)
# print(passed_students)

# lst = "Geeks For geeks"
# print(lst.split())
#
# sentence = "What is the Airspeed Velocity of  an Unladen Swallow?"
# print(sentence.split())
# result = {words: len(words) for words in sentence.split()}
# print(result)

# convert from Celsius to Fahrenheit.

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }


# weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)
#
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.item():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

# Another form of looping through a file such what I did in NATO_code.py (code line 8)
# {new_key:new_value for (index, row) in df.iterrows()}
