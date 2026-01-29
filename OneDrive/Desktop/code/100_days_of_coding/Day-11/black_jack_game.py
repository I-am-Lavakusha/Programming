import random
import art

def deal_card():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  card=random.choice(cards)
  return card

def scores(scores):
  if sum(scores)==21 and len(scores)==2:
    return 0
  if 11 in scores and sum(scores)>21:
    scores.remove(11)
    scores.append(1)

  return sum(scores)

def compare(u_score, c_score):
  if u_score==c_score:
    return "it's a draw"
  elif c_score==0:
    return "you lost as computer have a joker"
  elif u_score==0:
    return "you won as you had a joker"
  elif u_score>21:
    return "compurer won you lost"
  elif c_score>21:
    return "you won the game"
  elif u_score>c_score:
    return "you won"
  else:
    return "computer won"

def play_game():
  print(art.logo)
  user_cards=[]
  computer_cards=[]
  user_score=-1
  computer_score=-1
  should_play=False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not should_play:
    user_score=scores(user_cards)
    computer_score=scores(computer_cards)
    print(f"the current cards are {user_cards} and score is {user_score}")
    print(f"the computer first element is {computer_cards[0]}")
    
    if user_score==0 or computer_score==0 or user_score>21:
      should_play=True
    else:
      user_try=input("type 'y' to get another card or 'n' to pass: ")
      if user_try=='y':
        user_cards.append(deal_card())
      else:
        should_play=True

  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=scores(computer_cards)
    
  print(f"your final cards{user_cards} and score {user_score}")
  print(f"computer final cards{computer_cards} and score {computer_score}")
  print(compare(user_score, computer_score))

print("welcome to blackjack be aware of the rules and play")
while input("do you want to play the game 'y' or 'n' ")=='y':
  print("\n"*20)
  play_game()