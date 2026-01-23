def custom_name(f_name, l_name):
  return f"{f_name.title()} {l_name.title()}"

print(custom_name("gopal", "indhu"))


def function_1(text):
   return text+text

def function_2(text):
   return text.title()

print(function_2(function_1("hello")))



print(input("enter your f_name: "))

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)