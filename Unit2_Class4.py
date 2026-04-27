import random
def game_loop():
    print("Welcome to my rock,paper,scissors game")
   
     
    times_to_play= int(input("How many times do you want to play"))
    played=1
    
    computer_points = 0
    user_points = 0
    while played<=times_to_play:
        users_choice= input("Choose between rock,paper,scissors:")

        print("Your choice is:",users_choice)
        computer_options =["rock","paper","scissors","dragon"]



        computer_choice= random.choice(computer_options)
        print("Computers choice is:",computer_choice)

    


        if users_choice == "dragon" or users_choice == "Dragon":
            if computer_choice == "scissors":
                print("computer wins")
                computer_points = computer_points + 1
        if users_choice == "rock" or users_choice == "Rock":
            if computer_choice == "paper":
                print("computer wins")
                computer_points = computer_points + 1
            if computer_choice == "scissors":
                print("user wins")
                user_points = user_points+ 1
            if computer_choice == "rock":
                print("The game has been tied")
                

        elif users_choice == "paper" or users_choice == "Paper":
            if computer_choice == "rock":
                print("user wins")
                user_points = user_points+ 1

            if computer_choice == "scissors":
                print("computer wins")
                computer_points = computer_points + 1
            if computer_choice == "paper":
                print("The game has been tied")


        elif users_choice == "scissors" or users_choice == "Scissors":
            if computer_choice == "rock":
                print("computer wins")
                computer_points = computer_points + 1
            if computer_choice == "paper":
                print("user wins")
                user_points = user_points+ 1
            if computer_choice == "scissors":
                print("The game has been tied")

        else:
            print("You have entered an invalid option")

        print("User points are:",user_points)
        print("Computer points are:",computer_points)
        played=played+1

    ans=input("Do you want to continue")
    if ans=="yes":
        game_loop()

            


game_loop()

