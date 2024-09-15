# Get the user's age
age = int(input("Enter your age: "))

# Check if the age is 18 or above
if age >= 18:
    # Ask for nationality
    nationality = input("Do you have a Pakistani nationality? (yes/no): ").lower()
    
    # Check the nationality condition
    if nationality == "yes":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")
else:
    print("You are not eligible to vote yet.")
