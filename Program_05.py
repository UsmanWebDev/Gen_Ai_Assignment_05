# Get the year from the user
year = int(input("Enter a year: "))

# Check if the year is divisible by 4
if year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
