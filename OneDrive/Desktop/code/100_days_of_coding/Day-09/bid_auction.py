import art

print(art.logo)
print("Welcome to the auction")
bid=True

res={}
while bid:
  name=input("enter your name\n")
  amount=int(input("Enter the amount in dollars\n"))
  res[name]=amount
  first=input("Does anyone want to participate in the auction: 'yes' or 'no'\n").lower()
  if first=="no":
    print("Thank you for your participation wait for the results ")
    bid=False
  elif first=="yes":
    print("\n"*100)
  else:
    print("Invalid entry provide a valid entry")
    bid=False
winner=0
w_name=""
for key in res:
  if res[key]>winner:
    w_name=key
    winner=res[key]

print(f"the maximum bid is by {w_name} and the amount is ${res[w_name]}")



