def isValid(s):
    stack = []

    match = { ")": "(", "]": "[", "}": "{" }

    for letter in s:
        if letter == "(" or letter == "{" or letter == "[":
            stack.append(letter)
        elif letter == ")" or letter == "}" or letter == "]":
            if len(stack) == 0 or stack[len(stack) - 1] != match[letter]:
                return False
            stack.pop()
    
    return len(stack) == 0