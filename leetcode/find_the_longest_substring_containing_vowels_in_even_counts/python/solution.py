class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string, hash map
            A: bit manipulation, prefix sum, rolling hash
        """
        vowels = "aeiou"
        prefix_mask_index = {0: -1}
        res = 0
        mask = 0

        for index, letter in enumerate(s):
            if letter in vowels:
                shift = vowels.index(letter)
                mask ^= 1 << shift

                if mask not in prefix_mask_index:
                    prefix_mask_index[mask] = index

            res = max(res, index - prefix_mask_index[mask])

        return res


print(Solution().findTheLongestSubstring("eleetminicoworoep") == 13)
print(Solution().findTheLongestSubstring("leetcodeisgreat") == 5)
print(Solution().findTheLongestSubstring("bcbcbc") == 6)
