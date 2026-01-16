# Beckett Pizza Plaza – 4 for 3 Offer

## Introduction
This program uses Beckett Pizza Plaza “4-for-3” offer
to determine the total price of a pizza order. The customer decides to order 
four pizzas and the cheapest pizza is given for free.

The program is written in Python and is run using the terminal.

## How the Program Works

1. The program asks the user to enter the price of four pizzas.
2. Each input is checked to ensure it is a valid number greater than zero.
3. Invalid inputs (letters, zero, or negative numbers) are not accepted.
4. The prices are stored in a list.
5. The cheapest pizza price is found and removed from the total.
6. The final total and discount percentage are displayed.

## Discount Calculation
The cheapest pizza is free, and the discount percentage is automatically calculated as:
Example: If all pizzas cost £12, one £12 pizza is free → 25% discount.

## Input Validation
The program uses a loop and error handling to ensure only valid prices
are accepted. The user is repeatedly asked for input until a valid
price is entered.

## Technologies
- Python 3.x

## How to Run the Program (Terminal)

First Open the terminal in VS Code. Then, Navigate to the project folder containing `pizza.py`. 
Run the program using the command: python pizza.py

## Example Output (Valid Input)

Beckett Pizza Plaza 4-for-3 Offer
=================================
Enter Price of Pizza #1: 12
Enter Price of Pizza #2: 12
Enter Price of Pizza #3: 12
Enter Price of Pizza #4: 12
Your Total Order is £36.00, a fabulous discount of 25%!

Beckett Pizza Plaza 4-for-3 Offer
=================================
Enter Price of Pizza #1: 12.99
Enter Price of Pizza #2: 13.99
Enter Price of Pizza #3: 14.99
Enter Price of Pizza #4: 11.00
Your Total Order is £41.97, a fabulous discount of 21%!

## Example Output (Invalid Input)

Beckett Pizza Plaza 4-for-3 Offer
=================================
Enter Price of Pizza #1: 0
Invalid input! Please enter a number greater than 0.
Enter Price of Pizza #1: pepperoni
Invalid input! Please enter a valid number.
Enter Price of Pizza #1: 15.99

## Author
Suvana Gajurel