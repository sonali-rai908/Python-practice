import random

print("Snake_Water_Gun")

while True:
    user_score=0
    computer_score=0


    

    for round in range(1,4):
        print(f"\n=====Round {round}=====")
        options=["snake","water","gun"]

        user=input("\nEnter snake , water or gun: ").lower()
        computer=random.choice(options)

        print("Computer choice:",computer)

        if user not in options:
            print("Invalid input! No points awarded .")

        elif user == computer:
            print("\nMatch draw!")

        elif (user == "snake" and computer=="water") or (user=="water" and computer=="gun") or (user=="gun" and computer=="snake"):
            print("\nYou Win this round!")
            user_score+=1

        else:
            print("\nComputer wins this round!")   
            computer_score+=1

        print("\nYour score : ",user_score, "\nComputer score : ",computer_score)

    print("\n======FINAL RESULT======")    
    print("\nYour final score: ",user_score,"\nComputer final score: ",computer_score)
    if (user_score > computer_score):
        print("\nCongratulations!🥳 \nYou win the game!")

    elif(computer_score > user_score):
        print("\noohh no 😔! Computer won the game.\n No worries , better luck next time!")

    else:
        print("\nThe game is draw🤝!")    


    play_again=input("\nDo you want to play again? (yes/no) : ").lower()

    if play_again == "yes":
        continue
    else:
        print(" Thanks for playing!")
        break
            


