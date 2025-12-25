class TrieNode:
    def __init__(self) -> None:
        self.letters = {}
        self.is_word = False


class WordDictionary:
    """
    Time complexity:
        constructor: O(1)
        addWord: O(k)
        search: O(min(26^k, 26^w, n*k))
        n: word count
        k: word length
        w: windcard count
    Auxiliary space complexity: O(n*k)
    Tags: 
        DS: trie
        A: iteration, recursion
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
        def dfs(start: int, node: TrieNode) -> bool:
            for index in range(start, len(word)):
                letter = word[index]

                if letter in node.letters:
                    node = node.letters[letter]
                elif letter == ".":
                    for wild_card in node.letters.keys():
                        if dfs(index + 1, node.letters[wild_card]):
                            return True
                    return False
                else:
                    return False

            return node.is_word

        return dfs(0, self.root)


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "WordDictionary":
            cls = WordDictionary(*argument)
            output.append(None)
        elif operation == "addWord":
            cls.addWord(*argument)
            output.append(None)
        elif operation == "search":
            output.append(cls.search(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
    ["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
]

arguments_list = [
    [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]],
    [[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
]

expected_output_list = [
    [None,None,None,None,False,True,True,True],
    [None, None, None, True, True, False, True, False, False]
]


# Run tests
def run_tests(
        operations_list: list[list[str]],
        arguments_list: list[list[list[int]]],
        expected_output_list: list[list[int | None]],
        show_output: bool = False
) -> list[bool]:
    """
    Run a batch of TimeMap tests and compare outputs with expected results.
    If show_output is True, returns [(actual, expected), ...] instead of booleans.
    """
    output = []
    for operations, arguments, expected_output in zip(operations_list, arguments_list, expected_output_list):
        if show_output:
            output.append((test_input(operations, arguments), expected_output))
        else:
            output.append(test_input(operations, arguments) == expected_output)
    return output


print(run_tests(operations_list, arguments_list, expected_output_list, show_output=False))


# Example 1
word_dictionary = WordDictionary()
word_dictionary.addWord("a")
print(word_dictionary.search("a"))  # True
print(word_dictionary.search("b"))  # False
print(word_dictionary.search("."))  # True

# Example 1
word_dictionary = WordDictionary()
word_dictionary.addWord("bad")
word_dictionary.addWord("dad")
word_dictionary.addWord("mad")
print(word_dictionary.search("pad"))  # False
print(word_dictionary.search("bad"))  # True
print(word_dictionary.search(".ad"))  # True
print(word_dictionary.search("b.."))  # True
