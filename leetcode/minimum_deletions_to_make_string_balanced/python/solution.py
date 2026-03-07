class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        bees = 0
        res = 0

        for letter in s:
            if letter == "a":
                res = min(bees, res + 1)
            else:  # letter == "b":
                bees += 1

        return res


print(Solution().minimumDeletions("aababbab") == 2)
print(Solution().minimumDeletions("bbaaaaabb") == 2)
print(Solution().minimumDeletions("aabbbbaa") == 2)
