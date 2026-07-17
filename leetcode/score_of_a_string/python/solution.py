class Solution:
    def scoreOfString(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        N = len(text)
        res = 0

        for idx in range(N - 1):
            val1 = ord(text[idx])
            val2 = ord(text[idx + 1])
            res += abs(val1 - val2)

        return res


class Solution:
    def scoreOfString(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration, built-in function
        """
        return sum(abs(ord(text[idx]) - ord(text[idx + 1]))
                   for idx in range(len(text) - 1))


print(Solution().scoreOfString("hello") == 13)
print(Solution().scoreOfString("zaz") == 50)
