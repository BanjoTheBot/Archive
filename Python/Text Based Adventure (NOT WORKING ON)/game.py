def game () :
    from random import choice
    answer= input ("Welcome to A Game I Don't Know The Name of! Want to feel how painful it is playing a game made by someone with little to no expeirence? Yes or No?")

    if answer.lower () == "yes" :
        print("welcome to hell!")
        start=True
        inventory=[]
        choice = input("Press Enter to continue")
        if choice.lower () == "" :
            choiceY1=True 
    else: print("ok then, bitch.")

    if start==True:
        print ("")
        print("???: Hey, Hey dumbass, wake up")
        print("")
        print("???: Yeah, that's right, rise and shine, wake up, smell the ashes, yada yada.")
        print("")
        print("???: Ya shit's at the door, go grab it and get out, I don't care how hurt you are or how many of your memories you've lost, just get out of my house.")
        print("")
        choice = input("Press Enter to continue")
        if choice.lower () == "" :
            choiceY1=True 
            print("You get up, and walk down the hall and pick up your things. All that's left is your sword and a flask of water.")
            answer = input("Do you take your belongings? Y/N ")
            if answer.lower () == "y" :
                print("")
                print("#You obtained a Sword!")
                print("")
                print("#You obtained a flask of water!")
                print("")
            inventory.append("Sword")
            inventory.append("Flask of Water")
            choice = input("Press Enter to continue")
        if choice.lower () == "" :
            choiceY1=True 

        else: answer = input("You leave your items at the door and continue forward (Press Enter)")
        if choice.lower () == "" :
            choiceY1=True 
        
            print("")
            print("You step outside into the lush green forest, small woodland creatures run, bounce, and fly around, and the smell of the flowers float through the air.")
            print("")
            print("You follow the path through the forest, until you reach the top of the hill where the trees end")
            print("")
        choice = input("Press Enter to continue")
        if choice.lower () == "" :
            choiceY1=True 
            print("")
            print("You stroll down the hill and through the town gate, people are going about their days, shopping, playing, and doing whatever else they have to")
            print("")
            print("You hear some movement in an alleyway")
            choice = input("Press Enter to continue")
            
game ()
