def getLetterOccurences(s):
    occurences = [0] * 26

    for letter in s:
        index = ord(letter) - ord('a')
        occurences[index] += 1

    return occurences

def isAnagram(s, t):
    sOccurences = getLetterOccurences(s)
    tOccurences = getLetterOccurences(t)

    for i in range(26):
        if sOccurences[i] != tOccurences[i]:
            return False

    return True