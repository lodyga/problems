class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: recurnsion
        """
        letter_freq = {}

        for tile in tiles:
            letter_freq[tile] = letter_freq.get(tile, 0) + 1

        def backtrack():
            res = 0

            for letter in tuple(letter_freq.keys()):
                letter_freq[letter] -= 1
                
                if letter_freq[letter] == 0:
                    letter_freq.pop(letter)
                
                res += 1 + backtrack()
                letter_freq[letter] = letter_freq.get(letter, 0) + 1

            return res

        return backtrack()


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: recurnsion
        """
        letter_freq = [0] * 26

        for tile in tiles:
            index = ord(tile) - ord("A")
            letter_freq[index] += 1

        def backtrack():
            res = 0

            for index in range(26):
                if letter_freq[index] != 0:
                    letter_freq[index] -= 1
                    res += 1 + backtrack()
                    letter_freq[index] += 1

            return res

        return backtrack()


print(Solution().numTilePossibilities("AAB") == 8)
print(Solution().numTilePossibilities("AAABBC") == 188)
print(Solution().numTilePossibilities("V") == 1)
