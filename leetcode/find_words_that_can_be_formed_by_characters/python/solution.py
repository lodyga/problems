class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: hash map
        """
        def is_word_good(word: str) -> bool:
            freq_copy = char_letter_frequency.copy()

            for letter in word:
                if (letter not in freq_copy or
                        freq_copy[letter] == 0):
                    return False
                freq_copy[letter] -= 1

            return True

        char_letter_frequency = {}
        lengths_sum = 0

        for letter in chars:
            char_letter_frequency[letter] = char_letter_frequency.get(letter, 0) + 1

        for word in words:
            if is_word_good(word):
                lengths_sum += len(word)

        return lengths_sum


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: array
        """
        def is_word_good(word: str) -> bool:
            word_letter_frequency = [0] * 26

            for letter in word:
                word_letter_frequency[ord(letter) - ord("a")] += 1

            for index in range(26):
                if char_letter_frequency[index] < word_letter_frequency[index]:
                    return False

            return True

        lengths_sum = 0
        char_letter_frequency = [0] * 26

        for letter in chars:
            char_letter_frequency[ord(letter) - ord("a")] += 1

        for word in words:
            if is_word_good(word):
                lengths_sum += len(word)

        return lengths_sum


print(Solution().countCharacters(["cat", "bt", "hat", "tree"], "atach"), 6)
print(Solution().countCharacters(["hello", "world", "leetcode"], "welldonehoneyr"), 10)