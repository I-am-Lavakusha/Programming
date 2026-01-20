import random
words=["india", "pakisthan", "Bangladesh", "nepal","akaak"]
guess_the_word=random.choice(words).lower()
print(guess_the_word)

length=""
for i in range(len(guess_the_word)):
  length+="_"
print(f"The length of the word is: {length}")


flag=False
correct_list=[]
while not flag:
  letter=input("guess the letter: ")
  display=""
  for guess in guess_the_word:
    if guess==letter:
      display+=guess
      correct_list.append(guess)

    elif guess in correct_list:
      display+=guess
    else:
      display+="_"
  print(display)

  if "_" not in display:
    flag=True

  

