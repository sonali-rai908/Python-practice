import random
number = random.randint(1,100)

guesses = 0

while True: 
    guess =int(input("\nGusess a number between 1-100 : "))
    guesses += 1

    if (guess>number):
        print("Lower number please !")

    elif(guess<number):
        print("Higher number please !")

    else:
        print("\nCongratulations!!")
        print(f"\nComputer guess : {number}\nAnd now your gusess also : {guess} ")
        print(f"\nFinally you guesed the number in {guesses} guesses !")
        break

