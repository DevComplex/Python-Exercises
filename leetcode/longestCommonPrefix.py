class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordComplete = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            
            curr = curr.children[ch]

        curr.isWordComplete = True

    def longestCommonPrefix(self):
        prefix = ""

        curr = self.root

        while len(curr.children.keys()) == 1:
            for ch in curr.children.keys():
                prefix += ch
                curr = curr.children[ch]

                if curr.isWordComplete:
                    return prefix

        return prefix

def longestCommonPrefix(strs):
    trie = Trie()

    for string in strs:
        if string == "":
            return ""
        trie.add(string)

    return trie.longestCommonPrefix()

strs = ["dog", "dogq", "d"]

print(longestCommonPrefix(strs))


