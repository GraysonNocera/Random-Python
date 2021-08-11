# This program attempts to write code "pythonically"
from getpass import getpass
import datetime

"If/else structure in one line when assigning a variable"
condition = False

x = 1 if condition else 0

print(x)

"Using underscores to more easily read large values"
num1 = 100_000_000
num2 = 1_000_000_000_000
total = num1 + num2
print(f"{total:,}")

"Context managers"
with open('test.txt', 'w') as f:
    file_contents = f.write("Test")

"for loop using enumerate to get the index"
values = [34, 56, 12, 53, 98]
for index, value in enumerate(values):
    print(f"Value {value} at index {index}")

"for loop using zip to loop through more than one list"
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
for name, hero in zip(names, heroes):
    print(f"{name} is actually {hero}.")

# NOTES: zip returns a tuple of each value of each list at the given index


"Unpacking"
a, _ = (1, 3)
print(a)

a, b, *c, d = (1, 2, 3, 4, 5, 6)
print(c)
print(d)

# When we do not want to use a value we are unpacking, use an underscore to indicate it will not be used

"setattr and getattr"
class Person():
    pass

person = Person()
first_key = 'first'
first_val = 'Corey'

setattr(person, first_key, first_val)
print(person.first)

first = getattr(person, first_key)

print(person.first)

"Privacy when inputting password"
# password = getpass("Password: ")

"Running a module"
# python -m smtpd
# The -m denotes a module
# We can use this to run python files: instead of 'python pythonic.py', try 'python -m pythonic'

"Learn the functions that can be used from a module"
print(dir(datetime))
