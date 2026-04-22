class Solution:
    def characterReplacement(self, text: str, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array, string
            A: sliding window
        """
        window = [0] * 26
        left = 0
        # lazy upper bound
        most_freq = 1
        res = 1

        for right, letter in enumerate(text):
            idx = ord(letter) - ord("A")
            window[idx] += 1
            most_freq = max(most_freq, window[idx])

            while (right - left + 1) - most_freq > k:
                left_letter = text[left]
                idx = ord(left_letter) - ord("A")
                window[idx] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


print(Solution().characterReplacement("ABAB", 2) == 4)
print(Solution().characterReplacement("AABABBA", 1) == 4)
print(Solution().characterReplacement("BAAAB", 2) == 5)
