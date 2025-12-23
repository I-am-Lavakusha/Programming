def evalRPN(tokens):
        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(char))
                
        return stack[0]
tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))