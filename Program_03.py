# Get the user's age
age = int(input("Enter your age: "))

# Determine the age category
if 0 <= age <= 12:
    print("You are a Child.")
elif 13 <= age <= 19:
    print("You are a Teenager.")
elif 20 <= age <= 59:
    print("You are an Adult.")
elif age >= 60:
    print("You are a Senior Citizen.")
else:
    print("Invalid age entered. Please enter a valid age.")
