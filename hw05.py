# Here I rewrite hw05 from CS 159 in Python rather than C. This was one of the hardest
# assignments in all of CS 159, and it required hundreds of lines when written in C. 
# However, in Python, the assignment took less than 50 lines.

# This program prints a calendar given a year number and the occurence number, which
# signifies which week of the year needs to be printed
import datetime as dt

year = int(input("Enter year number -> "))
occurrence = int(input("Enter occurrence number -> "))
print()

# Get the date of Jan 1st of the year inputted by user
jan1 = dt.date(year, 1, 1)
tdelta = dt.timedelta((occurrence-1) * 7)
firstDay = jan1 + tdelta

tdelta = dt.timedelta(6)
lastDay = firstDay + tdelta

print(f"Start of week: {firstDay.strftime('%A')} {firstDay.strftime('%B')} {firstDay.day}, {firstDay.year}")
print(f"End of week: {lastDay.strftime('%A')} {lastDay.strftime('%B')} {lastDay.day}, {lastDay.year}\n")
print(firstDay.strftime('%B').center(27)) if len(firstDay.strftime('%B')) % 2 != 0 else print(firstDay.strftime('%B').center(26))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-\nSun Mon Tue Wed Thu Fri Sat")
print(" " + "    "*(firstDay.isoweekday() if firstDay.isoweekday() != 7 else 0), end="")

tdelta = dt.timedelta(1)

for index in range(7):
    if firstDay.isoweekday() > 6 and index != 0:
        print("\n ", end="")
    print(f"{firstDay.day:<4d}", end="")
    firstDay += tdelta

print()
