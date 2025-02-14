#Functions in Python
from sympy.physics.units import minutes


#simple funtion without arguments or any return value
def print_anything():
    print("Hello function")

print_anything()

#simple function with arguments
def printing(var):
    print(var, "welcome to python")

printing("Shehraz")

#simple function with return value
def print_anthing_return():
    return "Hello"

print(print_anthing_return(),"Shehraz")

#simple function with return value and arguments both
def addition(a,b):
    print("Summing both a and b")
    return a+b

Sum = addition(5,5.5)
print("sum is:",Sum)


# we can return multiple values also
def covert_seconds(seconds):
    hours = seconds // 3600  #floor division //
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds # will return a tuple

print(covert_seconds(5000))

hours, minutes, seconds = covert_seconds(5000)  # also can store in seperate variables
print(hours,minutes,seconds)