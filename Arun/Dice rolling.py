import random

print("Welcome to the Dice Simulator!")
print("You can roll the dice by pressing Enter.")

# Set up game loop
while True:
    input("Press Enter to roll the dice...")
    
    # Generate a random number between 1 and 6
    number = random.randint(1, 6)
    print("You rolled a", number)

    # Ask if the user wants to roll again
    roll_again = input("Do you want to roll again? (y/n): ")
    if roll_again != 'y':
        break

print("Thanks for playing!")