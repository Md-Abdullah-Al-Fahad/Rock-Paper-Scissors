import random

print("***** Let's play Rock Paper Scissors  *****")
pick = ["rock", "paper", "scissors"]
computer_won = 0
user_won = 0

while True:
    user_pick = input("Type rock, paper or scissors/ 'q' to quit : ")
    if user_pick == 'q':
        break
    random_number = random.randint(0,2)
    computer_guess = pick[random_number]

    if user_pick == 'rock' and computer_guess == 'scissors':
        print("You won!")
        user_won += 1
    elif user_pick == 'paper' and computer_guess == 'rock':
        print("You won!")
        user_won += 1
    elif user_pick == 'scissors' and computer_guess == 'paper':
        print("You won!")
        user_won += 1
    else:
        print("You lost!")
        computer_won += 1

    print(f"You won {user_won} times")
    print(f"Computer won {computer_won}")