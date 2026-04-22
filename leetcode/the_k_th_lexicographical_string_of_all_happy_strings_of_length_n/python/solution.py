class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list, string
            A: backtracking
        """
        chars = []

        def backtrack(idx, prev):
            nonlocal k
            if idx == n:
                k -= 1
                return not k

            for char in "abc":
                if char != prev:
                    chars.append(char)

                    if backtrack(idx + 1, char):
                        return True

                    chars.pop()

        backtrack(0, None)
        return "".join(chars)


print(Solution().getHappyString(1, 3) == "c")
print(Solution().getHappyString(1, 4) == "")
print(Solution().getHappyString(3, 9) == "cab")
