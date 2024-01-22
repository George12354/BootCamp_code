# "*arge" signifies an unlimited no of positional argument.
# "*arge" presents its data as a tuple(code line 4)
def add(*args):
    print(args)
    m = 0
    for n in args:
        m += n
    print(m)


add(7, 2)


# "**kwargs" also known as keyword argument
# Data here is presented in dictionary form(code line 16)

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# Here we created a class with an unlimited keyword argument

class Car:

    def __int__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        # self.model = kwargs["model"]
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")
# "get" is a function used for dictionary in other to get a variable, just like our square method.


my_car = Car(make="Nissan")
print(my_car.make)

# summary: The reason why you can't see any property to modify in tkinter and see things like:
# **kwargs, and *arge in the tkinter module, is because it was converted from another language and so
# all the option where packed in the position argument.
