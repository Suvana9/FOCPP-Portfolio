age = int(input("Enter your age: "))

if 18 <= age <= 30:
    print("you are still young!")
else:
    print("you are not in the young age range")

    age = int(input("Enter your age: "))

if age > 100:
    print("you are very old, well done!")
elif age > 80:
    print("you are fairly old")
elif age > 40:
    print("you are middle aged")
elif 30 <= age <= 40:
    print("you are entering middle age")
else:
    print("you are not very old yet")
