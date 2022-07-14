import random

#Starting program with variable for top end of range for numbers
top_of_range = input("Type a number: ")

#Ensuring input is a number and converting it to an integer
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

#Accounting for inputs less than zero, if less than 0 then program quits
    if top_of_range <= 0:
        print("Please type a larger number than 0 next time!")
        quit()

#Accounting for inputs that are not numbers and quitting otherwise
else:
    print("Please type a number next time!")
    quit()

#Creating range for numbers and printing random number
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

#Accounting for inputs that are not numbers and quitting otherwise
    else:
        print("Please type a number next time!")
        continue
# Ending the program if you user guesses the correct number
    if user_guess == random_number:
        print("YOU GOT IT!")
        break

# Helping user know if the number is higher or lower than their incorrect guess
    elif user_guess > random_number:
        print("A little lower!")
    else:
        print("A little higher!")

# Printing message and ending program when user guesses the correct number
print ("Wow, you got it right in", guesses, "guesses!")
quit()
