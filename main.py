import random

while True:
    choices = ['rock', 'paper', 'scissor']
    pcChoice = random.choice(choices)
    yourChoice = None

    while yourChoice not in choices:
        yourChoice = input('Rock, Paper or Scissor? ')

    print("PC: ", pcChoice)
    print("You: ", yourChoice)

    if yourChoice == pcChoice:
        print("Tie!")

    elif((yourChoice == 'rock' and pcChoice == 'scissor') or (yourChoice == 'paper' and pcChoice == 'rock') or (yourChoice == 'scissor' and pcChoice == 'paper')):
        print("You win!")
    else:
        print("You lose!")