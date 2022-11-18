from random import randint
from time import sleep
scorecomputer = 0
scoreuser = 0
chq = ""
while scorecomputer<3 or scoreuser<3:
  opponent = randint(1,3)
  
  print("Rock, Paper or Scissors?")
  print("Computer score:",scorecomputer,"/ Your score:",scoreuser)
  rps = input("Answer here: ")

  if rps == "rock":
    rps = 1
  elif rps == "paper":
    rps = 2
  elif rps == "scissors":
    rps = 3

  if opponent == 1:
    chq = "rock"
  elif opponent == 2:
    chq = "paper"
  elif opponent == 3:
    chq = "scissors"

  if rps == opponent:
    print("tie i also did",chq)
    scorecomputer = scorecomputer+1
    scoreuser = scoreuser+1
  elif rps == 1 and opponent == 2:
    print("i beat you i did",chq)
    scorecomputer = scorecomputer+1
  elif rps == 1 and opponent == 3:
    print("you beat me i did",chq)
    scoreuser = scoreuser+1
  elif rps == 2 and opponent == 1:
    print("you beat me i did",chq)
    scoreuser = scoreuser+1
  elif rps == 2 and opponent == 3:
    print("i beat you i did",chq)
    scorecomputer = scorecomputer+1
  elif rps == 3 and opponent == 1:
    print("you beat me i did",chq)
    scoreuser = scoreuser+1
  elif rps == 3 and opponent == 2:
    print("you beat me i did",chq)
    scoreuser = scoreuser+1
  else:
    print("you didnt put a valid answer.")

if scorecomputer > scoreuser:
  print("The computer won")
elif scorecomputer < scoreuser:
  print("You won")
elif scorecomputer == scoreuser:
  print("It was a tie")
print("Closing in 10 seconds")
sleep(1)
print("9")
sleep(1)
print("8")
sleep(1)
print("7")
sleep(1)
print("6")
sleep(1)
print("5")
sleep(1)
print("4")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1")
sleep(1)
