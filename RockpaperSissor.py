import random

print('lets play a ROCK PAPAER SCESSIOR')
print("you can select only from this option [ROCK ,PAPER,SCESSIOR]")
# ascii art of rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# ascii art of paper
paper= """
    _______
---'   ___)___
          ______)
          _______)
         _______)
---.__________)
"""
# ascii art of scissors
scissors = """
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
"""

while True:
    option = ['rock', 'paper', 'sciessor']
    # user enter his choice from option
    user_choice = input('enter your choice from [ROCK ,PAPER, SCESSIOR]=:')
    # computer choice will be pick by random module
    computer_turn = random.choice(option)
# condition for chosing user choice
    print('you chose')
    if user_choice == 'rock':
        print(rock)
    elif user_choice == 'paper':
        print(paper)
    else:
        print(scissors)
    # condtion for randomly choice by computer
    print('computer choice')
    if computer_turn == 'rock':
        print(rock)
    elif computer_turn == 'paper':
        print(paper)
    else:
        print(scissors)

    if user_choice == computer_turn:
        # if user and computer pick same option game will be tie
        print("its tie")
    #     if user choice rock and computer pick sciessor user won
    elif user_choice == 'rock' and computer_turn == 'sciessor':
        print("user WON!")
        # if user choice paper and computer pick rock user won
    elif user_choice == 'paper' and computer_turn == 'rock':
        print('user WON! ')
        # if user choice sciessor and computer paper user won
    elif user_choice == 'sciessor' and computer_turn == 'paper':
        print('user WON!')
    else:
        # in other condition computer won
        print("computer WON! ")
    # play again button if user wont play again say yes
    play_again = input('if you play again say  y/n::')
    if not play_again == 'y':
        break
print("thanks for playing")




