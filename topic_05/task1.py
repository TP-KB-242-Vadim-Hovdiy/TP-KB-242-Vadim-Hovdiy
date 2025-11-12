from random import choice

user_choice = input("Please enter one of the following: 'stone', 'scissor', 'paper': ").lower()

random_choice = choice(["stone", "scissor", "paper"])
print("Computer chose:", random_choice)

if user_choice == random_choice:
    print("It's a draw!")
elif (user_choice == "stone" and random_choice == "scissor") or \
     (user_choice == "scissor" and random_choice == "paper") or \
     (user_choice == "paper" and random_choice == "stone"):
    print("You win!")
elif user_choice in ["stone", "scissor", "paper"]:
    print("Computer wins!")
else:
    print("Invalid input! Please choose 'stone', 'scissor', or 'paper'.")
