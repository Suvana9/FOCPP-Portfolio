name = input("Enter your name: ")

if name != "":
    print("Your name is", name)
else:
    print("Name not entered")

    age = int(input("Enter your age: "))
print("you are an adult" if age >= 18 else "you are not an adult, yet!")