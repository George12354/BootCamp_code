# format to declare a data type for a variable
# age: int
# name: str
# height: float
# is_human: bool

# To specify the data type of the output of a function(return type), use ->(this feature is known as a type hint)
def police_check(age: int) -> bool:
    if age >= 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive


if police_check(19):
    print("You may pass")
else:
    print("Pay a fine")
