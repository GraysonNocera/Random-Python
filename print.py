# This program explores the print() function in Python

def main():

    i = 3
    # Three different ways to print something in python
    print(f"value of i is {i}.")
    print("value of i is " + str(i) + ".")
    print("value of i is {}.".format(i))

    if i > 3:
        print("i is not 3")
    else:
        print("i is what it is")



if __name__ == "__main__":
    main()