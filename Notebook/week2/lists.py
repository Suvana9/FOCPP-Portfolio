names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# First four primes
print("First four primes:", primes[:4])

# Insert two names before last name
names[-1:-1] = ["Tim", "Bill"]
print("Updated names:", names)

# Append
names.append("Brian")
print("After append:", names)

# List multiplication
nums = [1, 2, 3] * 5
print("Nums list:", nums)