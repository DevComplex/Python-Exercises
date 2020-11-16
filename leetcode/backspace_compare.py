def evaluate(S):
    s = []

    for ch in S:
        if ch == "#" and len(s) > 0:
            s.pop()
        elif ch != "#":
            s.append(ch)

    return "".join(s)

def backspace_compare(S, T):
    return evaluate(S) == evaluate(T)

S = "y#fo##f"
T = "y#f#o##f"
print(backspace_compare(S, T))