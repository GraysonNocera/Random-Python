# Here I explore python dictionaries

dictionary = {}

if "hi" in dictionary.keys():
    print(dictionary["hi"])


dictionary = {"hi": 1, "Hello": 2, "Goodbye": 3}

print(dictionary.keys())
print(dictionary.values())
for value in dictionary.values():
    print(value)

keys = dictionary.keys()


tempList = [("a", 1), ("b", 4), ("c", 0)]
print(tempList[1:])
tList = [("hi", 6), ("hello", 7)]
sortedList = sorted(tempList, key = lambda x: x[1], reverse=True)
print(sortedList)

sortedList[1:3] = tList
print(sortedList)


print(list(key for key in dictionary.keys()))
print(list(value for value in dictionary.values()))