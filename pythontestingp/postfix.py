def post_eval(s):
    stack= []
    for i in s:
        if i.isdigit():
            stack.append(i)
        elif i== "+":
            op1= stack.pop()
            op2= stack.pop()
            stack.append(op1) + (op2)
        elif i== "-":
            op1= stack.pop()
            op2= stack.pop()
            stack.append(op1)- (op2)
        elif i== "/":
            op1= stack.pop()
            op2= stack.pop()
            stack.append(op1)/ (op2)
        elif i== "*":
            op1= stack.pop()
            op2= stack.pop()
            stack.append(op1)* (op2)
        else:
            return "Invalid"    
    return stack

