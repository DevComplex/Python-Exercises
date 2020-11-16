import collections
import math

def toHex(num):
    if num == 0:
        return "0"
    if num < 0:
        num += int(math.pow(2, 32))

    values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    output = collections.deque()

    while num > 0:
        value = num % 16
        output.appendleft(values[value])
        num = num // 16

    return "".join(list(output))

num = -1

print(toHex(num))