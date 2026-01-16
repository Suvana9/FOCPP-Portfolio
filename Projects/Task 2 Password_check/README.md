# Password Check Program 

## Description
This Python program checks a user's password for security. It first verifies the length
of the password and then asks for specific letters to confirm the password.

The program works as follows:

1. User enters a password.
2. If the password is **shorter than 9 characters**, it shows `Password too short` and exits.
3. If the password is long enough, it asks for **letters at specific positions**.
4. If all letters are correct, it shows `Security check passed`.
5. If any letter is wrong, it shows `Security check failed` and exits.

## Requirements
- Python 3.x (tested on Python 3.8+).
- No external libraries are needed (uses built-in `random` and `sys` modules).

## How to Run
1. Open the folder in VS Code.
2. Open the terminal (**View → Terminal**).
3. Run the program with:

   ```bash
   python password_check.py

4. Follow the instructions to enter the password and requested letters.

## Example Outputs
### Case 1: Password too short
Enter your password: hello
Password too short.

### Case 2: Security check failed
Enter your password: Helloworlds
Enter letter at position 11: s
Correct
Enter letter at position 9: l
Correct
Enter letter at position 10: s
Security check failed.

### Case 3: Security check passed
Enter your password: helloworld
Enter letter at position 4: l
Correct
Enter letter at position 8: r
Correct
Enter letter at position 3: l
Correct
Security check passed.

## Notes
- Passwords are entered in plain text (visible on screen) for simplicity, as per the assignment.
- Positions are 1-based (e.g., position 1 is the first character).
- The program may ask for the same position multiple times randomly—handle it accordingly.
- This is for educational purposes only; in real applications, use secure password handling (e.g., hashing, no plain text).
- If you encounter issues, ensure Python is in your PATH and you're running from the correct directory.

## Author
Suvana Gajurel