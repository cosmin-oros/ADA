# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in
# a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object. void insert(String word) Inserts the string word into the trie. boolean search(
# String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix
# prefix, and false otherwise.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            # if the character is not in the children hashmap  then we create a new TrieNode else
            # we just move to the next node
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # we know we found the word if every character of the word is present in the hashmap and we reached the
        # end where we have endOfWord set to true
        return cur.endOfWord

    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # if we reach the end of the loop it means that all the characters in the prefix
        # are present in the hashmap so there is a word that starts with that prefix
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # return True
print(trie.search("app"))  # return False
print(trie.startsWith("app"))  # return True
trie.insert("app")
print(trie.search("app"))  # return True
