class TrieNode:
    """
    Trie node as hash map.
    """

    def __init__(self):
        self.letters = {}  # self.children = {}
        self.is_word = False


class Trie:
    """
    Time complexity:
        insert: O(n)
        search: O(n)
        startsWith: O(n)
        n: word length
    Auxiliary space complexity: O(t)
        t: number of Trie nodes
    Tags: trie as hash map
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def __contains__(self, word: str) -> bool:
        return self.search(word)

    def insert(self, word: str) -> None:
        node = self.root

        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()
            node = node.letters[letter]

        node.is_word = True

    def _find_node(self, word: str) -> bool:
        node = self.root

        for letter in word:
            if letter not in node.letters:
                return False
            node = node.letters[letter]

        return node

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node.is_word if node else False

    def startsWith(self, word: str) -> bool:
        node = self._find_node(word)
        return bool(node)


class TrieNode:
    """
    Trie node as list.
    """

    def __init__(self):
        self.letters = [None] * 26  # self.children = [] * 26
        self.is_word = False


class Trie:
    """
    Time complexity:
        insert: O(n)
        search: O(n)
        startsWith: O(n)
        n: word length
    Auxiliary space complexity: O(t)
        t: number of Trie nodes
    Tags: trie as hash map
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def __contains__(self, word: str) -> bool:
        return self.search(word)

    def insert(self, word: str) -> None:
        node = self.root

        for letter in word:
            index = ord(letter) - ord("a")
            if not node.letters[index]:
                node.letters[index] = TrieNode()
            node = node.letters[index]

        node.is_word = True

    def _find_node(self, word: str) -> bool:
        node = self.root

        for letter in word:
            index = ord(letter) - ord("a")
            if not node.letters[index]:
                return False
            node = node.letters[index]

        return node

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node.is_word if node else False

    def startsWith(self, word: str) -> bool:
        node = self._find_node(word)
        return bool(node)


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # return True
print(trie.search("app"))  # return False
print(trie.startsWith("app"))  # return True
trie.insert("app")
print(trie.search("app"))  # return True
print("app" in trie)  # return True