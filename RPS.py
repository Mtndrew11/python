import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print('You chose:')
if (userChoice == 0):
    print(rock)
elif (userChoice == 1):
    print(paper)
elif (userChoice ==2):
    print(scissors)

# random computer choice
computerChoice = random.randint(0, 2)
print("Computer chose:")
if (computerChoice == 0):
    print(rock)
elif (computerChoice == 1):
    print(paper)
elif (computerChoice ==2):
    print(scissors)


# Scissors (2) beats paper (1) beats rock (0)
if ( userChoice >= 3 or userChoice < 0 ):
    print("You typed an invalid number. You lose!")
elif ( userChoice == 0 and computerChoice == 2 ):
    print("You win!")
elif ( computerChoice == 0 and userChoice == 2 ):
    print("You lose!")
elif ( computerChoice > userChoice ):
    print("You lose!")
elif ( userChoice > computerChoice ):
    print("You win!")
elif ( userChoice == computerChoice ):
    print("It's a draw!")


# compare both
#if ( computerChoice == userInput_Lowercase ):
#    print('users choice was the same as the computer choice.')
#    print(f'User chose: {userInput_Lowercase}')
#    print(f'computer chose: {computerChoice}')
#
#else:
#    print(f'User chose: {userInput_Lowercase}')
#    print(f'computer chose: {computerChoice}')