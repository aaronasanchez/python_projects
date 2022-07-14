print("Welcome To BigBank")
Trials = 3
UserPin = 1234

#Starts the ATM process by asking for the bank PIN and assessing how many attempts are left to input the PIN correctly
while Trials != 0:
    Pin = int(input("Please Enter Your 4 Digit Pin Number: "))
#If the PIN is not entered correctly then the attemps drop by 1 and the "wrong pin number" message is displayed
    if Pin != UserPin:
        Trials -= 1
        print ("Wrong pin Number, You Have", Trials, "Trial(s) Left")
#If the PIN is entered correctly, the ATM asks the user to input whether they would like to withdraw or deposit
    else:
        UserChoice = input("d: Deposit or w: Withdraw: ")
#If the user chooses deposit, the ATM asks how much they would like to deposit. The user can then input a number to select how much they would to deposit
        if UserChoice == "d":
            UserDeposit = input("Enter The Amount You Would Like to Deposit: ")
#ATM prints the message to display how much you have deposited
            print(UserDeposit, "$ Have Been Deposited Into Your Account")
#if the user chooses "w" to withdraw, the ATM asks to input a number for withdrawal, then displays the withdrawal message with the amount that was withdrawn.
        if UserChoice == "w":
            UserWithdraw = input("Enter The Amount You Would Like to Withdraw: ")
            print(UserWithdraw, "$ Have Been Withdrawn From Your Account")
#After a withdrawal or a deposit, the ATM asks if you would like to continue
    UserExit = input("Would You Like To Continue? Y/N: ")
#If "N" is chosen the ATM thanks you for using the bank and exits the program
    if UserExit == "N":
        print("Thank You For Using BigBank")
        break
#If you choose "Y" then the ATM loops back to the start of the program where you have to input the correct PIN once again to access the ability to withdraw or deposit
    else:
        continue