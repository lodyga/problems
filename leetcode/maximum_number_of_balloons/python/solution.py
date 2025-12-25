class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: hash map
            A: iteration
        """
        letter_frequency = {}
        for letter in text:
            if letter in "balon":
                letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

        if len(letter_frequency) < 5:
            return 0

        counter = len(text)
        for letter, frequency in letter_frequency.items():
            if letter in "ban":
                counter = min(counter, frequency)
            else:
                counter = min(counter, frequency >> 1)

        return counter


print(Solution().maxNumberOfBalloons("nlaebolko") == 1)
print(Solution().maxNumberOfBalloons("loonbalxballpoon") == 2)
print(Solution().maxNumberOfBalloons("leetcode") == 0)
print(Solution().maxNumberOfBalloons("balon") == 0)
print(Solution().maxNumberOfBalloons("lloo") == 0)
