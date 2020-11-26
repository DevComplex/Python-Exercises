def toGoatLatin(S):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    output = []

    words = S.split()

    for i, word in enumerate(words):
        letters = list(word)

        if word[0].lower() in vowels:
            letters.append("ma")
        else:
            letters = letters[1:] + letters[:1] + ["ma"]

        extra = ["a"] * (i + 1)

        letters.extend(extra)

        output.append("".join(letters))

    return " ".join(output)

s = "I speak Goat Latin"

print(toGoatLatin(s))