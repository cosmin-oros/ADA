class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class TrieTree:
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            
        node.is_end_of_word = True

    def get_all_words(self):
        words = []
        self._get_all_words(self.root, "", words)
        # we use the function sorted to return the words in alphabetical order
        return sorted(words)

    def _get_all_words(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)

        # c - the character, child_node - the Node of that word
        for c, child_node in node.children.items():
            self._get_all_words(child_node, prefix + c, words)


trie_tree = TrieTree()
trie_tree.add_word("Ana")
trie_tree.add_word("are")
trie_tree.add_word("mere")
trie_tree.add_word("si")
trie_tree.add_word("pere")

print(trie_tree.get_all_words())