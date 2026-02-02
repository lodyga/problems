class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Time complexity: O(w*n2*3^k)
            n: board length
            k: word length
            w: word count
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: backtracking
        """
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]

        def backtrack(index, row, col):
            if index == len(word):
                return True
            elif (
                row == -1 or
                col == -1 or
                row == ROWS or
                col == COLS or
                board[row][col] != word[index] or
                visited[row][col]
            ):
                return False

            visited[row][col] = True
            is_found = False

            for dr, dc in DIRECTIONS:
                (r, c) = (row + dr, col + dc)
                if backtrack(index + 1, r, c):
                    is_found = True
                    break

            visited[row][col] = False
            return is_found

        word_found = []
        for word in words:
            is_added = False
            for row in range(ROWS):
                if is_added:
                    break
                for col in range(COLS):
                    if backtrack(0, row, col):
                        word_found.append(word)
                        is_added = True
                        break

        return word_found


class TrieNode:
    def __init__(self) -> None:
        self.letters = {}
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()
            node = node.letters[letter]
        node.is_word = True

    def has(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.letters:
                return False
            node = node.letters[letter]
        return node.is_word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Time complexity: O(n2*3^k + w)
            n: board length
            k: longest word length
            w: word count
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: backtracking
        """
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]
        LONGEST = max(len(word) for word in words)

        trie = Trie()
        for word in words:
            trie.add(word)

        def backtrack(index, row, col, node, word):
            if (
                index == LONGEST or
                row == -1 or
                col == -1 or
                row == ROWS or
                col == COLS or
                visited[row][col] or
                board[row][col] not in node.letters
            ):
                return

            visited[row][col] = True
            letter = board[row][col]
            word = word + letter
            node = node.letters[letter]

            if node.is_word:
                word_found.add(word)

            for dr, dc in DIRECTIONS:
                (r, c) = (row + dr, col + dc)
                backtrack(index + 1, r, c, node, word)

            visited[row][col] = False

        word_found = set()
        for row in range(ROWS):
            for col in range(COLS):
                backtrack(0, row, col, trie.root,  "")

        return list(word_found)


class TrieNode:
    def __init__(self) -> None:
        self.letters = {}
        self.is_word = False
        self.word_index = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.word_index = 1

    def add(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()
            node = node.letters[letter]
        node.is_word = True
        node.word_index = self.word_index
        self.word_index += 1

    def has(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.letters:
                return False
            node = node.letters[letter]
        return node.is_word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Time complexity: O(n2*3^k + w)
            n: board length
            k: longest word length
            w: word count
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array (matrix)
            A: backtracking
        """
        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited_cells = set()
        words_found = set()

        trie = Trie()
        word_index_map = {}
        word_index = 1
        for word in words:
            trie.add(word)
            word_index_map[word_index] = word
            word_index += 1

        def backtrack(row, col, node):
            if (
                row < 0 or
                col < 0 or
                row == ROWS or
                col == COLS or
                board[row][col] not in node.letters or
                (row, col) in visited_cells
            ):
                return False

            visited_cells.add((row, col))
            letter = board[row][col]
            if node.letters[letter].is_word:
                words_found.add(
                    word_index_map[node.letters[letter].word_index])

            for dr, dc in DIRECTIONS:
                (r, c) = (row + dr, col + dc)
                backtrack(r, c, node.letters[letter])
            visited_cells.remove((row, col))
            return False

        for row in range(ROWS):
            for col in range(COLS):
                backtrack(row, col, trie.root)

        return list(words_found)


print(sorted(Solution().findWords([["a", "b"], ["a", "d"]], ["aa", "ab"])) == sorted(["aa", "ab"]))
print(sorted(Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"])) == sorted(["oath", "eat"]))
print(sorted(Solution().findWords([["a", "b"], ["c", "d"]], ["abcd"])) == sorted([]))
print(sorted(Solution().findWords([["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]], ["oa", "oaa"])) == sorted(["oa", "oaa"]))
print(sorted(Solution().findWords([["a", "b"], ["a", "a"]], ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"])) == sorted(["aba", "aaa", "aaab", "baa", "aaba"]))
