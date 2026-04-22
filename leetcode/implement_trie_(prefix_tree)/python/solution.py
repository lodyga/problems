class TrieNode:
    def __init__(self) -> None:
        self.letters = {}
        self.is_word = False


class Trie:
    """
    Time complexity:
        insert: O(n)
        search: O(n)
        startsWith: O(n)
        n: word length
    Auxiliary space complexity: O(t)
        t: number of trie nodes
    Tags: 
        DS: trie, hash map
        A: iteration
    """

    def __init__(self):
        self.root = TrieNode()

    def __contains__(self, item: str) -> bool:
        return self.search(item)

    def insert(self, word: str) -> None:
        node = self.root

        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()

            node = node.letters[letter]

        node.is_word = True

    def lookup_node(self, word) -> TrieNode | None:
        node = self.root

        for letter in word:
            if letter not in node.letters:
                return None

            node = node.letters[letter]

        return node

    def search(self, word: str) -> bool:
        node = self.lookup_node(word)
        return node.is_word if node else False

    def startsWith(self, prefix: str) -> bool:
        return bool(self.lookup_node(prefix))


trie = Trie()
trie.insert("apple")
print(trie.search("apple") is True)
print(trie.search("app") is False)
print(trie.startsWith("app") is True)
trie.insert("app")
print(trie.search("app") is True)
print("apple" in trie)
