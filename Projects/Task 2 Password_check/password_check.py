import random  # Import random module for generating random positions
import sys     # Import sys module for exiting the program on failure

# Prompt the user to enter their password
password = input("Enter your password: ")

# Check if the password is at least 9 characters long; if not, inform and exit
if len(password) < 9:
    print("Password too short.")
    sys.exit()

# Loop three times to ask for random letters from the password
for _ in range(3):
    # Generate a random 1-based position within the password's length
    pos = random.randint(1, len(password))
    
    # Prompt the user for the letter at that position
    letter = input(f"Enter letter at position {pos}: ")
    
    # Check if the entered letter matches the actual letter (using 0-based indexing)
    if letter != password[pos - 1]:
        print("Security check failed.")
        sys.exit()  # Exit immediately on incorrect answer
    else:
        print("Correct")  # Confirm correct answer

# If all checks pass, print success message
print("Security check passed.")