#Q)Develop a rock, paper and scissors game using if-else
import random

choices = ["rock","paper","scissors"]  #this is called list similar to arraylists in java or vector in C++
# random.choice() is a function that randomly picks anything from lists, tuples or a character from string
computer = random.choice(choices)

user_choice = input("Choose Rock, Paper or Scissors: ")
user_choice = user_choice.lower() #or directly do this while taking input -> input("Etc").lower()

if user_choice not in choices:
    print("Invalid Input!")
elif user_choice == computer:
    print(f"It's a Draw!,Computer Also Chose {computer}")
elif ((user_choice == choices[0] and computer == choices[2]) or
      (user_choice == choices[1] and computer == choices[0]) or
      (user_choice == choices[2] and computer == choices[1])):
    print(f"You Won!,Computer Chose {computer}")
else:
    print(f"You Lose!,Computer Chose {computer}")