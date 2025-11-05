class Solution:
    def minOperations(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        zero = 0  # target 0101...
        one = 0  # target 1010...

        for index, char in enumerate(text):
            if index % 2:
                # 0101...
                if char == "0":
                    zero += 1
                # 1010...
                else:
                    one += 1
            else:
                # 0101...
                if char == "1":
                    zero += 1
                # 1010...
                else:
                    one += 1

        return min(zero, one)


print(Solution().minOperations("0100") == 1)
print(Solution().minOperations("10") == 0)
print(Solution().minOperations("1111") == 2)
