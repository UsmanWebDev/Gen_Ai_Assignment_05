# Get the month number from the user
month = int(input("Enter a month (1-12): "))

# Determine the number of days in the month
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("This month has 31 days.")
elif month in [4, 6, 9, 11]:
    print("This month has 30 days.")
elif month == 2:
    print("This month has 28 days (non-leap year).")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
