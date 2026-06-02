class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: iteration
        """
        LETTERS = "ablno"
        letter_freq = {letter: 0 for letter in LETTERS}
        res = len(text)

        for letter in text:
            if letter in letter_freq:
                letter_freq[letter] += 1

        for letter, freq in letter_freq.items():
            if letter in "lo":
                res = min(res, freq // 2)
            else:
                res = min(res, freq)

        return res


print(Solution().maxNumberOfBalloons("nlaebolko") == 1)
print(Solution().maxNumberOfBalloons("loonbalxballpoon") == 2)
print(Solution().maxNumberOfBalloons("leetcode") == 0)
print(Solution().maxNumberOfBalloons("balon") == 0)
print(Solution().maxNumberOfBalloons("lloo") == 0)
