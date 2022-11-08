input("Welcome to [INSERT BANKING BRAND HERE] ATM!")
Trials = 3
UserPin = 1243
balance=3000

while Trials != 0:
    Pin = int(input("Please input 4 digit PIN: "))
    if Pin != UserPin:
        Trials -= 1
        print("You have entered the incorrect PIN, you have", Trials, "retry's left")
    else:
        while True:
            UserChoice = input("1: Deposit.\n2: Withdrawl.\n3: Check Balance.\n4: Exit ATM\n> ")
            
            if UserChoice == "1":
                UserDeposit = input("Enter the desired amount to deposit ")
                balance += int(UserDeposit)
                print ("$",UserDeposit, "dollars have been deposited")
            
            if UserChoice == "2":
                UserWithdraw = input("Enter the desired amount to withdraw ")
                if int(UserWithdraw) > balance:
                    print("ERROR! YOU DONT HAVE ENOUGH MONEY TO WITHDRAW, COME BACK WHEN YOURE RICH" )
                else:
                    balance -= int(UserWithdraw)
                    print ("$",UserWithdraw, "has been withdrawn")
            
            if UserChoice == "3":
                print ("Your current balance is : ",balance,".")
            
            if UserChoice == "4":
                print("Thank you for using [INSERT BANKING BRAND HERE], have a wonderful day!")
                exit(0)