# Get input from user
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")

# Check if the number is positive, negative, or zero
if num > 0:
    print(f"{num} is a Positive number.")
elif num < 0:
    print(f"{num} is a Negative number.")
else:
    print(f"{num} is Zero.")

# Check divisibility by 2 and 3
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by both 2 and 3.")
elif num % 2 == 0:
    print(f"{num} is divisible by 2 but not by 3.")
elif num % 3 == 0:
    print(f"{num} is divisible by 3 but not by 2.")
else:
    print(f"{num} is not divisible by either 2 or 3.")
