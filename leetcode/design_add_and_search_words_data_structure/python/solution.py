class TrieNode:
    def __init__(self) -> None:
        self.letters = {}
        self.is_word = False


class WordDictionary:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags: trie
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()
            node = node.letters[letter]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(left, node):
            for right, letter in enumerate(word[left:], left):
                if letter == ".":
                    return any(dfs(right + 1, value_node) 
                               for value_node in node.letters.values())
                    
                elif letter in node.letters:
                    node = node.letters[letter]
                else:
                    return False
            return node.is_word

        return dfs(0, self.root)


word_dictionary = WordDictionary()
word_dictionary.addWord("a")
print(word_dictionary.search("a")) # True
print(word_dictionary.search("b")) # False
print(word_dictionary.search(".")) # True

word_dictionary = WordDictionary()
word_dictionary.addWord("bad")
word_dictionary.addWord("dad")
word_dictionary.addWord("mad")
print(word_dictionary.search("pad")) # False
print(word_dictionary.search("bad")) # True
print(word_dictionary.search(".ad")) # True
print(word_dictionary.search("b..")) # True