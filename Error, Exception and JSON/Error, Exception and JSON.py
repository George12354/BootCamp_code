# JSON: Originally created for javaScript, is also the standard way of transferring data across the internet

# Exception
# In Python, an exception is an event that occurs during the execution of a program and disrupts the normal flow
# of the program's instructions. When an exception is raised, the normal flow of the program is interrupted, and
# the Python interpreter looks for an exception handler that can handle the specific type of exception.
# If a suitable handler is found, it is executed to deal with the exceptional situation; otherwise, the program
# terminates, and an error message is displayed.

# They are four main keyword in exception:
# try:except:else:finally
# try: This is a code that is most likely not working to work, this type of code might cause an exception.
# except: If the code in try fails, the keyword is here to work in place of it.
# else: When the code in "try" work, this keyword is here is run after it. Here no exception.
# finally: This code run no matter the case. Exception or no Exception.



# sample cod
# try:
#     # Code that may raise an exception
#     x = int(input("Enter a number: "))
#     result = 10 / x
#     print("Result:", result)
#
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
#
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
#
# else:
#     print("No exceptions occurred.")
#
# finally:
#     print("This block always executes, whether there was an exception or not.")
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     print("File was closed")
#     raise TypeError
# # Last keyword: raise-- allow one to create an exception.

height = float(input("Height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
