print("Welcome to my UFC quiz!")

playing = input("Type 'yes' if you would like to play! : ")

if playing.lower() != "yes":
    quit()

print("Okay then, let's play!")
score = 0

answer = input("Which middleweight champion in the UFC had the longest title reign in the history of the promotion?: ")
if answer.lower() == "anderson silva":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("Who was the flyweight champion before Henry Cejudo beat them to attain the championship belt?: ")
if answer.lower() == "demetrious johnson":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("Who was the head coach of the GOAT fighter GSP while he was actively fighting?: ")
if answer.lower() == "firas zahabi":
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

answer = input("Who is the GOAT?: ")
if answer.lower() == "gsp":
    print("CORRECT!")
    score += 1

else:
    print("INCORRECT!")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score/4 * 100) + "%!")