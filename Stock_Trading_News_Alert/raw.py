from datetime import datetime

def print_day_with_zeros(date_string):
    # Convert the date string to a datetime object
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    # Extract the day with leading zeros
    day_with_zeros = date_obj.strftime('%d')
    month_with_zeros = date_obj.strftime('%m')
    print(day_with_zeros)
    print(date_obj)

# Example usage
date_string = '2024-04-05'
print_day_with_zeros(date_string)


# from datetime import datetime
#
# # Define the string representing the date/time
# date_string = "2024-04-15 08:30:00"
#
# # Define the format of the date/time string
# date_format = "%Y-%m-%d %H:%M:%S"
#
# # Parse the string into a datetime object
# parsed_date = datetime.strptime(date_string, date_format)
#
# # Now you can work with the parsed datetime object
# print(parsed_date)  # Output: 2024-04-15 08:30:00
