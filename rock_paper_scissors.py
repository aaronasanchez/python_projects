import random

#Sets the win counter for the player and the computer to zero
user_wins = 0
computer_wins = 0

#Makes a list of rock paper and scissors, storing them within the integers 0, 1 and 2
options = ["rock", "paper", "scissors"]

#Runs the starting message and instructs the player on what to type to play and what to type to exit the game
while True:
    user_input = input("Type Rock/Paper/Scissors to play. Or type Q to quit: ").lower()
    # If the user types q, the program ends
    if user_input == "q":
        break
    
    # Sends an error message and restars the program if a non valid command is entered
    if user_input not in options:
        print ("Please enter a valid command")
        continue
    
    #Sets the variable random_number to store a random integer between 0 and 2
    random_number = random.randint(0, 2)
                                         # rock: 0, paper: 1, scissors: 2
    #The computer picks a number between 0 and 2 to decide whether it chooses rock, paper, or scissors
    computer_pick = options[random_number]
    # prints what the computer picked
    print("Computer picked", computer_pick + ".")

    # Lines 31-57 are all of the possibilities for what the player could input and what the computer could pick
    #If the user guesses correctly to beat the computer the game prints the victory message and increases the user_wins variable score by 1.
    if user_input == "rock" and computer_pick == "scissors":
        print ("YOU WON!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick == "rock":
        print ("YOU WON!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print ("YOU WON!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print ("DRAW!")
        user_wins += 0

    elif user_input == "paper" and computer_pick == "paper":
        print ("DRAW!")
        user_wins += 0

    elif user_input == "rock" and computer_pick == "rock":
        print ("DRAW!")
        user_wins += 0

    #If the computer wins, the computer_wins variable increases it's score by 1
    else:
        print("YOU LOST!")
        computer_wins += 1

# Once the player quits the game, prints the score for the computer and the player. Then thanks the user for playing.
print ("You won", user_wins, "times.")
print ("The computer won", computer_wins, "times.")
print("Goodbye and thanks for playing!")
