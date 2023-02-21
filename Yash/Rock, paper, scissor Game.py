import random

print("Welcome to my Rock, Paper, Scissor Game")
print("Let's Start Playing :)")

print("R = Rock")
print("P = Paper")
print("S = Scissor")

while True:
    comp_choice = random.choice(['R', 'P', 'S'])
    player_choice = input("Write R/P/S :")

    print("Your Choice: " + player_choice.upper())
    print("Computer's Choice: " + comp_choice)

    if comp_choice == player_choice.upper():
        print("DRAW")
    elif (comp_choice == 'R' and player_choice.upper() == 'P') or (comp_choice == 'P' and player_choice.upper() == 'S') or (comp_choice == 'S' and player_choice.upper() == 'R'):
        print("You Won")
    else:
        print("You Lost")

    restart = input("Restart the game (y/n): ")
    if restart != "y":
        break

print("Thank you for Playing :)")