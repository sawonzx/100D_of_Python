import random

# emoji's
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

# User_input
choices = [rock, paper, scissors]
user = int(input("What do you choose?\n1.Rock\n2.Paper\n3.Scissors\nYou Chose: "))
print(choices[user -1])


computer = random.randint(1, 3)
print("Computer Chose: \n" , choices[computer-1])

if user > 3 or user < 1:
    print("You typed an invalid number. You lose!")
elif user == 1 and computer == 3:
    print("You win!")
elif computer == 1 and user == 3:
    print("You lose!")
elif computer > user:
    print("You lose!")
elif user > computer:
    print("You win!")
elif computer == user:
    print("It's a draw!")

#---------End_of_File---------
