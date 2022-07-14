#Sets your name for the adventure and welcomes you to the adventure
name = input("Type your name: ")
print("Welcome", name, "to this grand adventure!")

# The first choice of the adventure
answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

# Presents the choices if you choose left
if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    # Provides different outcomes based on whether you choose to walk around or swim across the river.
    if answer == "swim":
        print("You swam acrross and were eaten by a great white shark. What is a shark doing in a river anyways? YOU LOSE!")
    elif answer == "walk":
        print("You walked for many miles and ran out of water. You collapsed due to dehydration. YOU LOSE!")
    else:
        print('Not a valid option. You lose.')

# Presents the choices if you choose right
elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    # Provides different outcomes based on whether you choose to walk across the bridge or not.
    if answer == "back":
        print("You go back, deterred by the threat that the wobbly bridge presents. You decide that adventuring is not for you after all, especially if there are things scarier than a wobbly bridge. YOU LOSE!")

    # Moves the story forward if you decide to cross the bridge
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        # Presents the options if you cross the bridge. This is the final option that could result either a win or a loss.
        if answer == "yes":
            print("You talk to the stanger and they reveal to you that they are a seasoned adventurer themselves. They give you all of the knowledge that you could possibly need to become a great adventurer like them. You follow their words of wisdom and become the greatest adventurer in the history of the world. YOU WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are so offended that they fire a magical spell from the finger between their index and ring fingers. You are knocked into the river and eaten by a great white shark. What is a shark doing in a river anyways? YOU LOSE!")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

# Thanks the user for adventuring and exits the program.
print("Thank you for adventuring", name + "!")