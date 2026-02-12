class Solution:
    def numTrees(self, n: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        memo = [-1] * max(2, (n + 1))
        memo[0] = 1
        memo[1] = 1

        def dfs(n):
            if memo[n] != -1:
                return memo[n]

            res = 0
            for index in range(n):
                left = dfs(index)
                right = dfs(n - index - 1)
                res += left * right

            memo[n] = res
            return res

        return dfs(n)


class Solution:
    def numTrees(self, n: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        # {[index]: number of unique BSTs with index nodex}
        cache = [1] * (n + 1)

        for index in range(2, n + 1):
            res = 0

            for i in range(index):
                left = cache[i]
                right = cache[index - i - 1]
                res += left * right

            cache[index] = res

        return cache[n]


print(Solution().numTrees(1) == 1)
print(Solution().numTrees(2) == 2)
print(Solution().numTrees(3) == 5)
print(Solution().numTrees(19) == 1767263190)
