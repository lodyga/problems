class Solution:
    def countGoodSubstrings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: iteration
        """
        N = len(text)
        res = 0

        for idx in range(N - 2):
            char1 = text[idx]
            char2 = text[idx + 1]
            char3 = text[idx + 2]

            if (
                char1 != char2
                and char1 != char3
                and char2 != char3
            ):
                res += 1

        return res


class Solution:
    def countGoodSubstrings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: iteration
        """
        N = len(text)
        res = 0

        for index in range(N - 2):
            if len(set(text[index: index + 3])) == 3:
                res += 1

        return res


print(Solution().countGoodSubstrings("xyzzaz") == 1)
print(Solution().countGoodSubstrings("aababcabc") == 4)
print(Solution().countGoodSubstrings("x") == 0)
