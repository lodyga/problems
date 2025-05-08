class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash map
        """
        letter_frequency = {}
        letters = "balon"
        balloon_count = len(text)

        for letter in text:
            if letter in "balon":
                letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

        for letter in letters:
            if letter not in letter_frequency:
                return 0

        for key, val in letter_frequency.items():
            if key in "lo":
                balloon_count = min(balloon_count, val // 2)
            else:
                balloon_count = min(balloon_count, val)

        return balloon_count


print(Solution().maxNumberOfBalloons("nlaebolko"), 1)
print(Solution().maxNumberOfBalloons("loonbalxballpoon"), 2)
print(Solution().maxNumberOfBalloons("leetcode"), 0)
print(Solution().maxNumberOfBalloons("balon"), 0)
print(Solution().maxNumberOfBalloons("lloo"), 0)