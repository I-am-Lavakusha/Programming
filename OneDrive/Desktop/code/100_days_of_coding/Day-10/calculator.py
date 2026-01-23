import art
def add(n1, n2):
  return n1+n2
def sub(n1, n2):
  return n1-n2
def mul(n1, n2):
  return n1*n2
def div(n1, n2):
  return n1/n2 

operations={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div,
}

def calculator():
  print(art.logo)
  should_accumulate=True
  num1=float(input("Enter the number: "))
  while should_accumulate:
    for key in operations:
      print(key)

    operation=input("select the operation: ")
    num2=float(input("Enter the second number: "))
    answer=operations[operation](num1,num2)
    print(f"{num1} {operation} {num2} = {answer}")
    choice=input(f"do you want to continue with the same {answer} 'yes' or 'no' ")
    if choice == "yes":
      num1=answer
    else:
      should_accumulate=False
      print("\n"*20)
      calculator()

calculator()