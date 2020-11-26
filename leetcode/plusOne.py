import collections

def plusOne(digits):
    output = collections.deque()
    carry = 1

    for i in range(len(digits) -1, -1, -1):
        carry += digits[i]
        digit = carry % 10
        carry = carry // 10
        output.appendleft(digit)

    if carry > 0:
        output.appendleft(carry)

    return list(output)

digits = [9, 9, 9]

print(plusOne(digits))