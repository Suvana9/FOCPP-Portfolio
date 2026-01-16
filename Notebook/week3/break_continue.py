numbers = [10, 20 , 30, 90, 200, 30, 22, 11]
total = 0

for num in numbers:
    total += num
    print("Running total:", total)

numbers = [10, 20 , 30, 90, 200, 30, 22, 11]
total = 0

for num in numbers:
    if num > 100:
        print("Value over 100 found – stopping loop")
        break
    total += num
    print("Running total:", total)

numbers = [10, 20 , 30, 90, 30, 22, 11]
total = 0

for num in numbers:
    if num > 100:
        print("Value over 100 found – stopping loop")
        break
    total += num
else:
    print("all numbers processed")

print("Final total:", total)