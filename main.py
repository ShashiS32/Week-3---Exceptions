try:
    x = int(input("What is x? "))
    print (f"x is {x}")
except ValueError:
    print("X needs to be an int, you didnt write an int")
    