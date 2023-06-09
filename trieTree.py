class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def _get_all_words(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)
        sorted_children = sorted(node.children.items(), key=lambda x: x[0])
        for char, child in sorted_children:
            self._get_all_words(child, prefix + char, words)

    def get_all_words(self):
        words = []
        self._get_all_words(self.root, '', words)
        return words

    def remove_word(self, word):
        def _remove_helper(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            should_remove_child = _remove_helper(node.children[char], word, index + 1)
            if should_remove_child:
                del node.children[char]
                return len(node.children) == 0

            return False

        _remove_helper(self.root, word, 0)


trie = Trie()
trie.add_word("banana")
trie.add_word("apple")
trie.add_word("grape")
trie.add_word("orange")
trie.add_word("pear")

# printing all words in alphabetical order
all_words = trie.get_all_words()
print("All words:", all_words)

# removing a word
trie.remove_word("banana")
print("Words after removing 'banana':", trie.get_all_words())
