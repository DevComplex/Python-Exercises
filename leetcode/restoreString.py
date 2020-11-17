def restoreString(s, indices):
    newStr = [0] * len(s)

    for i in range(len(s)):
        letter = s[i]
        index = indices[i]
        newStr[index] = letter

    return "".join(newStr)

s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]

print(restoreString(s, indices))