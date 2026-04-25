
import random

print("Welcome to my rock,paper,scissors game")

computer_points = 0
user_points = 0

users_choice= input("Choose between rock,paper,scissors:")

print("Your choice is:",users_choice)
computer_options =["rock","paper","scissors"]



computer_choice= random.choice(computer_options)
print("Computers choice is:",computer_choice)



if users_choice == "rock":
    if computer_choice == "paper":
        print("Computer Wins")
        computer_points = computer_points+1
    if computer_choice == "scissors":
        print("User wins")
        user_points=user_points+1
        
    if computer_choice== "rock":
        print("the game has been tied")
        
        

if users_choice == "paper":
    if computer_choice == "rock":
        print("User Wins")
        user_points=user_points+1
    if computer_choice =="scissors":
        print("Computer wins")
        computer_points = computer_points+1
        
if users_choice =="scissors":
    if computer_choice == "rock":
        print("Computer wins")
        computer_points = computer_points+1
    if computer_choice == "paper":
        print("User wins")
        user_points=user_points+1

print("User points are:",user_points)
print("Computer points are:",computer_points)


    


