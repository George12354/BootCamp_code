print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
tip = 1+(float(input("How much tip would you like to give? 10, 12, or 15? "))/100)
split = float(input("How many people to split the bill? "))

total = round((total_bill/split) * tip, 2)
print(f"Each person should pay: ${total} ")
