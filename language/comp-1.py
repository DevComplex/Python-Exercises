def identity(nums):
    return [num for num in nums]

def doubled(nums):
    return [2 * num for num in nums]

def squared(nums):
    return [num * num for num in nums]

def evens(nums):
    return [num for num in nums if num % 2 == 0]

def odds(nums):
    return [num for num in nums if num % 2 == 1]

def positives(nums):
    return [num for num in nums if num > 0]

def selective_stringify_nums(nums):
    return [str(num) for num in nums if num % 5 == 0]

def words_not_the(sentence):
    return [len(word) for word in sentence.split() if word != "the"]

def vowels(word):
    return [char for char in word if char in {"a", "i", "e", "o", "u"}]

def vowels_set(word):
    return {char for char in word if char in {"a", "i", "e", "o", "u"}}

def disemvowel(sentence):
    return "".join([char for char in sentence if char not in {"a", "i", "e", "o", "u"}])

def wiggle_numbers(nums):
    return [2 * num if num % 2 == 0 else -num for num in nums]

def encrypt_lol(sentence):
    return "".join([chr(1 + ord(char)) if char != " " and ord(char) - ord("a") >= 0 and ord(char) - ord("a") <= 24 else char for char in sentence])
