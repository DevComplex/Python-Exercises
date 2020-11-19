def getTotal(vals):
    total = 0

    for val in vals:
        total += val
    
    return total

def calPoints(ops):
    stack = []

    for op in ops:
        if op == "C" and len(stack) > 0:
            stack.pop()
        elif op == "D":
            val = stack[len(stack) - 1]
            stack.append(val * 2)
        elif op == "+":
            val1 = stack[len(stack) - 1]
            val2 = stack[len(stack) - 2]
            stack.append(val1 + val2)
        elif op != "C" and op != "D" and op != "+":
            stack.append(int(op))
    
    return getTotal(stack)

ops = ["5", "2", "C", "D", "+"]

print(calPoints(ops))