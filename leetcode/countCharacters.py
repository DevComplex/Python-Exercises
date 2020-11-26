import collections

def countCharacters(words, chars):
    charsCount = collections.Counter(chars)
    output = 0

    for word in words:
        hasWord = True
        wordCharsCount = collections.Counter(word)

        for letter, count in wordCharsCount.items():
            if not (letter in charsCount and count <= charsCount[letter]):
                hasWord = False
                break

        if hasWord:
            output += len(word)

    return output


words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

print(countCharacters(words, chars))