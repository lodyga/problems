class Solution:
    def countPalindromicSubsequence(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: prefix sum
            A: iteration
        """
        prefix_sum = []
        prefix = [0] * 26
        for letter in text:
            index = ord(letter) - ord("a")
            prefix = prefix.copy()
            prefix[index] += 1
            prefix_sum.append(prefix)

        palindrome_set = set()
        for middle in range(1, len(text) - 1):
            left_prefix = prefix_sum[middle - 1]
            right_suffix = [prefix_sum[-1][index] - prefix_sum[middle + 0][index]
                            for index in range(26)]
            diff = [right_suffix[index] > 0 and left_prefix[index] > 0
                    for index in range(26)]
            for index in range(26):
                if diff[index]:
                    palindrome = chr(index + ord("a")) + text[middle]
                    palindrome_set.add(palindrome)

        return len(palindrome_set)


print(Solution().countPalindromicSubsequence("aabca") == 3)
print(Solution().countPalindromicSubsequence("adc") == 0)
print(Solution().countPalindromicSubsequence("bbcbaba") == 4)
