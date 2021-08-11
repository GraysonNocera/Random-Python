# This program takes as input a list of letters and returns the letters that did not 
# appear in that input list. This was used for a single purpose but can become more
# versatile by altering the variable charsTotal

charsTaken = input("Input letters used: ").split(",")
charsTakenSet = set(charsTaken)

charsTotal = ['p', 'i', 'n', 'k', ' ', 'c', 'a', 'r', 'e', ' ', 'b', 'e', 'a', 'r']
charsTotalSet = set(charsTotal)

print("Letters to still use")

for char in charsTotalSet:
    if charsTotal.count(char) != charsTaken.count(char):
        if char == " ":
            print("space " * (charsTotal.count(char) - charsTaken.count(char)), end="")
        else:
            print(f"{char} " * (charsTotal.count(char) - charsTaken.count(char)), end="")

print()
