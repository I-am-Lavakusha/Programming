import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scizzer='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to rock paper scizzer game")

choice=int(input("Enter 0 for rock, 1 for paper 2 for scizer: \n"))
computer_choice=random.randint(0,2)
list1=[rock, paper, scizzer]
if choice<0 or choice>2:
  print("Invalid choice you lost!")

else:
  print(f"Your choice: \n {list1[choice]}")
  print(f"computer choice: \n {list1[computer_choice]}")

  if choice==computer_choice:
    print("It's a draw")

  elif choice==1 and computer_choice==0:
    print("you won!")

  elif choice==2 and computer_choice==1:
    print("you won!")

  elif choice==0 and computer_choice==2:
    print("you won!")

  else:
    print("computer won!")
