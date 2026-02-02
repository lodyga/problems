class Solution:
    def maxDifference(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        letter_freq = [0] * 26
        for letter in text:
            letter_ind = ord(letter) - ord("a")
            letter_freq[letter_ind] += 1

        max_odd_freq = 1
        min_even_fre = len(text)

        for freq in letter_freq:
            if freq % 2:
                max_odd_freq = max(max_odd_freq, freq)
            elif freq:
                min_even_fre = min(min_even_fre, freq)

        return max_odd_freq - min_even_fre


print(Solution().maxDifference("aaaaabbc") == 3)
print(Solution().maxDifference("abcabcab") == 1)
print(Solution().maxDifference("yzyyys") == -3)
print(Solution().maxDifference("sssgssiisisiggigsigiiigigggigiggsigggggigsigsisgsgiissisgsiggigssgsgisiisgsgggiigiiggiii") == -3)
