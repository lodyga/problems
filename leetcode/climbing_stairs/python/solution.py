class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force, pure recursion
        """
        def dfs(idx):
            if idx >= n:
                return idx == n

            return dfs(idx + 1) + dfs(idx + 2)

        return dfs(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force, shared state
        """
        res = 0

        def dfs(idx):
            nonlocal res
            if idx >= n:
                res += (1 if idx == n else 0)
                return

            dfs(idx + 1)
            dfs(idx + 2)

        dfs(0)
        return res


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        memo = [-1] * n
        memo.append(1)
        memo.append(0)

        def dfs(idx):
            if memo[idx] != -1:
                return memo[idx]

            memo[idx] = dfs(idx + 1) + dfs(idx + 2)
            return memo[idx]

        return dfs(0)


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [0] * n
        cache.append(1)
        cache.append(0)

        for idx in range(n - 1, -1, -1):
            cache[idx] = cache[idx + 1] + cache[idx + 2]

        return cache[0]


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [1, 0]

        for _ in range(n - 1, -1, -1):
            cache[0], cache[1] = cache[0] + cache[1], cache[0]

        return cache[0]

    def climbStairs(self, num: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bottom-up
        """
        a = 0
        b = 1

        for _ in range(num):
            (a, b) = (b, a + b)
            # b = a + b
            # a = b - a
        return b


print(Solution().climbStairs(1) == 1)
print(Solution().climbStairs(2) == 2)
print(Solution().climbStairs(3) == 3)
print(Solution().climbStairs(4) == 5)
print(Solution().climbStairs(5) == 8)
print(Solution().climbStairs(6) == 13)
print(Solution().climbStairs(44) == 1134903170)
