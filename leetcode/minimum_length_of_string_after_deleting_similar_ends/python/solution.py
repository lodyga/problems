class Solution:
    def minimumLength(self, s: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, two pointers
        """
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            char = s[left]

            while left <= right and s[left] == char:
                left += 1

            while left <= right and s[right] == char:
                right -= 1

        return right - left + 1


print(Solution().minimumLength("a") == 1)
print(Solution().minimumLength("aa") == 0)
print(Solution().minimumLength("aabaaa") == 1)
print(Solution().minimumLength("ca") == 2)
print(Solution().minimumLength("cabaabac") == 0)
print(Solution().minimumLength("aabccabba") == 3)
print(Solution().minimumLength("abbbbbbbbbbbbbbbbbbba") == 0)
