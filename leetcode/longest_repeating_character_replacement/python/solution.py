class Solution:
    def characterReplacement(self, word: str, joker: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: sliding window as hash map
        """
        window = {}
        left = 0
        longest = 0
        most_frequent = 0  # lazy upper bound

        for right, letter in enumerate(word):
            window[letter] = window.get(letter, 0) + 1
            most_frequent = max(most_frequent, window[letter])

            while (right - left + 1) - most_frequent > joker:
                left_letter = word[left]
                window[left_letter] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


class Solution:
    def characterReplacement(self, word: str, joker: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: brute-force
        """
        longest = 0

        for left in range(len(word)):
            counter = {}
            most_frequent = 0

            for right in range(left, len(word)):
                letter = word[right]
                counter[letter] = counter.get(letter, 0) + 1
                most_frequent = max(most_frequent, counter[letter])
                if (right - left + 1) - most_frequent > joker:
                    break

                longest = max(longest,
                              min(most_frequent + joker, right - left + 1))

        return longest


print(Solution().characterReplacement("ABAB", 2) == 4)
print(Solution().characterReplacement("AABABBA", 1) == 4)