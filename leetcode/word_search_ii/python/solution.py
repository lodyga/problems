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
        def backtrack(row: int, col: int, idx: int, word: str) -> bool:
            if idx == len(word):
                return True
            elif (
                row in (-1, ROWS)
                or col in (-1, COLS)
                or board[row][col] != word[idx]
                or visited[row][col]
            ):
                return False

            visited[row][col] = True
            is_found = False

            for dr, dc in DIRECTIONS:
                (r, c) = (row + dr, col + dc)

                if backtrack(r, c, idx + 1, word):
                    is_found = True
                    break

            visited[row][col] = False
            return is_found

        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]
        res = []

        for word in words:
            is_word_found = False

            for row in range(ROWS):
                if is_word_found:
                    break

                for col in range(COLS):
                    if backtrack(row, col, 0, word):
                        res.append(word)
                        is_word_found = True
                        break

        return res


class aTrieNode:
    def __init__(self) -> None:
        self.letters: dict = {}
        self.word_idx: int = -1


class aTrie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str, word_idx: int) -> None:
        node = self.root

        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()

            node = node.letters[letter]

        node.word_idx = word_idx


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Time complexity: O(n2*3^k + c)
            n: board length
            k: longest word length
            c: letter count
            w: word count
        Auxiliary space complexity: O(n2 + w)
        Tags:
            DS: array (matrix)
            A: backtracking
        """
        def backtrack(row: int, col: int, node: TrieNode) -> None:
            if (
                row in (-1, ROWS)
                or col in (-1, COLS)
                or board[row][col] not in node.letters
                or visited[row][col]
            ):
                return

            visited[row][col] = True
            letter = board[row][col]
            next_node = node.letters[letter]

            # Remove dead branches from the Trie.
            if not next_node.letters and next_node.word_idx == -1:
                del node.letters[letter]

            if next_node.word_idx != -1:
                res_idx.append(next_node.word_idx)
                next_node.word_idx = -1
            
            for dr, dc in DIRECTIONS:
                backtrack(row + dr, col + dc, next_node)

            visited[row][col] = False

        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]
        res_idx = []
        trie = Trie()

        for word_idx, word in enumerate(words):
            trie.add(word, word_idx)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] in trie.root.letters:
                    backtrack(row, col, trie.root)

        return [words[idx] for idx in res_idx]


class TrieNode:
    def __init__(self) -> None:
        self.letters: dict = {}
        self.word_idx: int = -1

    def add(self, word: str, word_idx: int) -> None:
        node = self

        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()

            node = node.letters[letter]

        node.word_idx = word_idx


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Time complexity: O(n2*3^k + c)
            n: board length
            k: longest word length
            c: letter count
            w: word count
        Auxiliary space complexity: O(n2 + w)
        Tags:
            DS: array (matrix)
            A: backtracking
        """
        def backtrack(row: int, col: int, node: TrieNode) -> None:
            if (
                row in (-1, ROWS)
                or col in (-1, COLS)
                or board[row][col] not in node.letters
                or visited[row][col]
            ):
                return

            visited[row][col] = True
            letter = board[row][col]
            next_node = node.letters[letter]

            # Remove dead branches from the Trie.
            if not next_node.letters and next_node.word_idx == -1:
                del node.letters[letter]

            if next_node.word_idx != -1:
                res_idx.append(next_node.word_idx)
                next_node.word_idx = -1
            
            for dr, dc in DIRECTIONS:
                backtrack(row + dr, col + dc, next_node)

            visited[row][col] = False

        ROWS = len(board)
        COLS = len(board[0])
        DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = [[False] * COLS for _ in range(ROWS)]
        res_idx = []
        trie_root = TrieNode()

        for word_idx, word in enumerate(words):
            trie_root.add(word, word_idx)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] in trie_root.letters:
                    backtrack(row, col, trie_root)

        return [words[idx] for idx in res_idx]


print(sorted(Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"])) == sorted(["oath", "eat"]))
print(sorted(Solution().findWords([["a", "b"], ["c", "d"]], ["abcd"])) == sorted([]))
print(sorted(Solution().findWords([["a", "b"], ["a", "d"]], ["aa", "ab"])) == sorted(["aa", "ab"]))
print(sorted(Solution().findWords([["a", "b"], ["a", "d"]], ["aa", "ab"])) == sorted(["aa", "ab"]))
print(sorted(Solution().findWords([["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]], ["oa", "oaa"])) == sorted(["oa", "oaa"]))
print(sorted(Solution().findWords([["a", "b"], ["a", "a"]], ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"])) == sorted(["aba", "aaa", "aaab", "baa", "aaba"]))
