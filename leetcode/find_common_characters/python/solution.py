class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        """
        Time complexity: O(n*m)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list, array, string
            A: iteration
        """
        letters = [100] * 26
        res = []

        for word in words:
            letter_freq = [0] * 26

            for letter in word:
                idx = ord(letter) - ord("a")
                letter_freq[idx] += 1

            for idx in range(26):
                letters[idx] = min(letters[idx], letter_freq[idx])

        for idx in range(26):
            if letters[idx]:
                for _ in range(letters[idx]):
                    res.append(chr(idx + ord("a")))
        
        return res


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        """
        Time complexity: O(n*m)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, list, string
            A: iteration
        """
        letters = {}
        res = []
        
        for letter in words[0]:
            letters[letter] = letters.get(letter, 0) + 1

        for word in words:
            letter_freq = {}

            for letter in word:
                letter_freq[letter] = letter_freq.get(letter, 0) + 1

            for letter in letters:
                if letter in letter_freq:
                    letters[letter] = min(letters[letter], letter_freq[letter])
                else:
                    letters[letter] = 0

        for letter, freq in letters.items():
            if freq:
                for _ in range(freq):
                    res.append(letter)
        
        return res


print(Solution().commonChars(["bella", "label", "roller"]) == ["e", "l", "l"])
print(Solution().commonChars(["cool", "lock", "cook"]) == ["c", "o"])
