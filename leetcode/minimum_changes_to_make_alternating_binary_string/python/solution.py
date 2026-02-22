class Solution:
    def minOperations(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        diff_a = 0
        diff_b = 0

        for index in range(len(text)):
            a = "0" if index % 2 else "1"
            b = "1" if index % 2 else "0"
            diff_a += 1 if text[index] != a else 0
            diff_b += 1 if text[index] != b else 0

        return min(diff_a, diff_b)


print(Solution().minOperations("0100") == 1)
print(Solution().minOperations("10") == 0)
print(Solution().minOperations("1111") == 2)
