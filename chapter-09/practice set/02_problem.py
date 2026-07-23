''' The game() function in a program lets a user play a game and returns the score 
  as an integer. You need to read a file "Hi-score.txt" which is eithr blank
  or contains the previous Hi-score.You need to write a program to update the Hi-score whenever te game() 
  function breaks the Hi-score. '''
import random

def game():
  print("You are playing game....")
  score=random.randint(1,62)

  # fetch the highscore
  with open("high_score.txt") as file:
    highscore=file.read()

    if(highscore!=""):
      highscore=int(highscore)
    else:
      highscore=0

  print(f"Your score: {score}")

  if (score>highscore):
    # update the new highscore to the file
    with open("high_score.txt","w") as file:
      file.write(str(score))

  return score

game()
  