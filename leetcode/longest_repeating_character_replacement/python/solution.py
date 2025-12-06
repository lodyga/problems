class Solution:
    def characterReplacement(self, text: str, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: array
            A: sliding window
        """
        window = [0] * 26
        left = 0
        # lazy upper bound
        most_frequent = 1
        longest = 1

        for right, letter in enumerate(text):
            index = ord(letter) - ord("A")
            window[index] += 1
            most_frequent = max(most_frequent, window[index])

            while (right - left + 1) - most_frequent > k:
                left_letter = text[left]
                left_index = ord(left_letter) - ord("A")
                window[left_index] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


class Solution:
    def characterReplacement(self, word: str, joker: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: hash map
            A: brute-force
        """
        longest = 0

        for left in range(len(word)):
            letter_frequency = {}
            most_frequent = 0

            for right in range(left, len(word)):
                letter = word[right]
                letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
                most_frequent = max(most_frequent, letter_frequency[letter])
                if (right - left + 1) - most_frequent > joker:
                    break

                longest = max(
                    longest,
                    min(most_frequent + joker, right - left + 1)
                )

        return longest


print(Solution().characterReplacement("ABAB", 2) == 4)
print(Solution().characterReplacement("AABABBA", 1) == 4)
