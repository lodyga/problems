class Solution:
    def maxDifference(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        frequencies = [0] * 26
        max_odd_freq = 0
        min_even_freq = len(text)

        def letter_index(letter):
            return ord(letter) - ord("a")

        for letter in text:
            frequencies[letter_index(letter)] += 1
        
        for frequency in frequencies:
            if not frequency:
                continue
            elif frequency & 1:
                max_odd_freq = max(max_odd_freq, frequency)
            else:
                min_even_freq = min(min_even_freq, frequency)

        return max_odd_freq - min_even_freq


print(Solution().maxDifference("aaaaabbc") == 3)
print(Solution().maxDifference("abcabcab") == 1)
print(Solution().maxDifference("yzyyys") == -3)