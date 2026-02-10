from game_data import data
import random
from art import logo, vs

def format_data(account):
  account_name=account["name"]
  account_desr=account["description"]
  account_country=account["country"]
  return f"{account_name}, a {account_desr}, from {account_country}"

def check_answer(guess, a_follower_count, b_follower_count):
  if a_follower_count > b_follower_count and guess=="a":
    return guess=='a'
  else:
    return guess=='b'

print(logo)
current_score=0
game_should_continue=True
account_b=random.choice(data)

while game_should_continue:
  account_a=account_b
  account_b=random.choice(data)
  if account_a==account_b:
    account_b=random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  guess=input("who has more followers 'A' or 'B' ").lower()

  print('\n'*20)
  print(logo)
  a_follower_count=account_a['follower_count']
  b_follower_count=account_b['follower_count']

  is_correct=check_answer(guess, a_follower_count, b_follower_count)

  if is_correct:
    current_score+=1
    print(f"you are right and current score is {current_score}")
  else:
    print(f"you are wrong and the final score is {current_score}")
    game_should_continue=False


