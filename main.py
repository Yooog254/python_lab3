# Prompt the user to enter a number of pennies, nickels, dimes, quarters.
PENNIES = float(input("Enter the number of pennies: "))
NICKELS = float(input("Enter the number of nickels: "))
DIMES = float(input("Enter the number of dimes: "))
QUARTERS = float(input("Enter the number of quarters: "))

# Declare constants
PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

# Calculating the value of each amount of pennies, nickels, dimes, and quarters.
PENNIES *= PENNY
NICKELS *= NICKEL
DIMES *= DIME
QUARTERS *= QUARTER

total = PENNIES + NICKELS + DIMES + QUARTERS

if total == 1.00:
    print("You Won! The amount entered equals $1.00.")
elif total > 1.00:
    print(f"The amount entered is greater than $1.00: ${total:.2f}.")
    print("You lost.")
else:
    print(f"The amount entered is less than $1.00: ${total:.2f}.")
    print("You lost.")
