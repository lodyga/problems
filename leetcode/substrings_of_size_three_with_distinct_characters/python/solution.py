class Solution:
    def countGoodSubstrings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: string
            A: iteration
        """
        res = 0

        for idx in range(len(text) - 2):
            substr = text[idx: idx + 3]

            if (
                substr[0] != substr[1] and
                substr[0] != substr[2] and
                substr[1] != substr[2]
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
        res = 0

        for index in range(len(text) - 2):
            if len(set(text[index: index + 3])) == 3:
                res += 1

        return res


print(Solution().countGoodSubstrings("xyzzaz") == 1)
print(Solution().countGoodSubstrings("aababcabc") == 4)
