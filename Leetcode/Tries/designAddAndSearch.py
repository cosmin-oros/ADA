# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object. void addWord(word) Adds word to the data structure, it can be matched
# later. bool search(word) Returns true if there is any string in the data structure that matches word or false
# otherwise. word may contain dots '.' where dots can be matched with any letter.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndOfWord = True

    def search(self, word):
        def dfs(j, root):
            cur = root

            for i in range(len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEndOfWord
        return dfs(0, self.root)


obj = WordDictionary()
obj.addWord("bad")
param_1 = obj.search("bad")
obj.addWord("dad")
param_2 = obj.search("dad")
obj.addWord("mad")
param_3 = obj.search("mad")
print(param_1)
print(param_2)
print(param_3)
