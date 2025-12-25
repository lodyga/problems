class Solution:
    def tribonacci(self, num: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: hash map
            A: top-down
        """
        memo = {0: 0, 1: 1, 2: 1}

        def dfs(num):
            if num in memo:
                return memo[num]

            memo[num] = dfs(num - 1) + dfs(num - 2) + dfs(num - 3)
            return memo[num]

        return dfs(num)


class Solution:
    def tribonacci(self, num: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: list
            A: bottom-up
        """
        cache = [0, 1, 1]

        for index in range(3, num + 1):
            cache.append(cache[index - 1] +
                         cache[index - 2] +
                         cache[index - 3]
                         )

        return cache[num]


class Solution:
    def tribonacci(self, num: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: array
            A: bottom-up
        """
        cache = [0, 1, 1]

        for index in range(3, num + 1):
            cache[index % 3] = cache[0] + cache[1] + cache[2]

        return cache[num % 3]


print(Solution().tribonacci(0) == 0)
print(Solution().tribonacci(3) == 2)
print(Solution().tribonacci(4) == 4)
print(Solution().tribonacci(25) == 1389537)
print(Solution().tribonacci(31) == 53798080)
print(Solution().tribonacci(35) == 615693474)
