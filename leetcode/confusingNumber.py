def confusingNumber(N):
    valid = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6"
    }

    invalid = set(["2", "3", "4", "5", "7"])

    output = []

    for digit in str(N):
        if digit in invalid:
            return False

        output.append(valid[digit])

    output = int("".join(output[::-1]))

    return int(output) != N

print(confusingNumber(916))