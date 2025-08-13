class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Time complexity: O(wnm*3^k)
            k: word length
            w: word count
        Auxiliary space complexity: O(nm)
        Tags: backtracking
        """
        rows = len(board)
        cols = len(board[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited_cells = set()
        words_found = set()

        def dfs(row, col, index):
            if index == len(word):
                return True
            elif (
                row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                board[row][col] != word[index] or
                (row, col) in visited_cells
            ):
                return False

            visited_cells.add((row, col))
            for r, c in directions:
                if dfs(row + r, col + c, index + 1):
                    return True
            visited_cells.remove((row, col))
            return False

        for row in range(rows):
            for col in range(cols):
                for word in words:
                    if dfs(row, col, 0):
                        words_found.add(word)
                        visited_cells = set()

        return list(words_found)


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

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.letters:
                return False
            node = node.letters[letter]
        return node.is_word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Time complexity: O(nm*3^k)
            k: word length
        Auxiliary space complexity: O(nm)
        Tags: backtracking, trie
        """
        rows = len(board)
        cols = len(board[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited_cells = set()
        words_found = set()

        word_trie = Trie()
        for word in words:
            word_trie.add(word)

        def dfs(row, col, node, word):
            if (
                row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                board[row][col] not in node.letters or
                (row, col) in visited_cells
            ):
                return False

            visited_cells.add((row, col))
            word += board[row][col]
            if node.letters[board[row][col]].is_word:
                words_found.add(word)
            
            for r, c in directions:
                dfs(row + r, col + c, node.letters[board[row][col]], word)
            visited_cells.remove((row, col))
            return False

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, word_trie.root, "")

        return list(words_found)


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

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.letters:
                return False
            node = node.letters[letter]
        return node.is_word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Time complexity: O(nm*3^k)
            k: word length
        Auxiliary space complexity: O(nm)
        Tags: backtracking, trie
        """
        rows = len(board)
        cols = len(board[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited_cells = set()
        words_found = set()

        word_trie = Trie()
        word_index_map = {}
        word_index = 1
        for word in words:
            word_trie.add(word)
            word_index_map[word_index] = word
            word_index += 1

        def dfs(row, col, node):
            if (
                row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                board[row][col] not in node.letters or
                (row, col) in visited_cells
            ):
                return False

            visited_cells.add((row, col))
            if node.letters[board[row][col]].is_word:
                words_found.add(word_index_map[node.letters[board[row][col]].word_index])
            
            for r, c in directions:
                dfs(row + r, col + c, node.letters[board[row][col]])
            visited_cells.remove((row, col))
            return False

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, word_trie.root)

        return list(words_found)


print(Solution().findWords([["a", "b"], ["a", "d"]], ["aa", "ab"]), ["aa", "ab"])
print(Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]), ["oath", "eat"])
print(Solution().findWords([["a", "b"], ["c", "d"]], ["abcd"]), [])
print(Solution().findWords([["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]], ["oa", "oaa"]), ["oa", "oaa"])