class Solution:
    def tribonacci(self, number: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        cache = [0, 1, 1]
        if number < 3:
            return cache[number]
        
        for _ in range(3, number + 1):
            cache = [cache[1], cache[2], sum(cache)]

        return cache[-1]


class Solution:
    def tribonacci(self, number: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up, fancy
        """
        triplet = [0, 1, 1]

        for index in range(3, number + 1):
            triplet[index % 3] = sum(triplet)

        return triplet[number % 3]


class Solution:
    def tribonacci(self, number: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        cache = [None] * (number + 1)
        cache[:3] = [0, 1, 1]
        if number < 3:
            return cache[number]
        
        for index in range(3, number + 1):
            cache[index] = cache[index - 1] + cache[index - 2] + cache[index - 3]

        return cache[number]


class Solution:
    def tribonacci(self, number: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {0: 0, 1: 1, 2: 1}
        
        def dfs(index):
            if index in memo:
                return memo[index]
            
            memo[index] = dfs(index - 1) + dfs(index - 2) + dfs(index - 3)
            return memo[index]

        return dfs(number)


class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as list
        """
        memo = [None] * (n + 1)
        memo[:3] = [0, 1, 1]

        def dfs(index):
            if memo[index] is not None:
                return memo[index]

            memo[index] = dfs(index - 1) + dfs(index - 2) + dfs(index - 3)
            return memo[index]

        return dfs(n)


class Solution:
    def tribonacci(self, number: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        memo = {0: 0, 1: 1, 2: 1}
        
        def dfs(index):
            if index in memo:
                return memo[index]
            
            return dfs(index - 1) + dfs(index - 2) + dfs(index - 3)

        return dfs(number)


class Solution:
    def tribonacci(self, number: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        memo = [0, 1, 1]
        
        def dfs(index):
            if index < 3:
                return memo[index]
            
            return dfs(index - 1) + dfs(index - 2) + dfs(index - 3)

        return dfs(number)


print(Solution().tribonacci(0), 0)
print(Solution().tribonacci(3), 2)
print(Solution().tribonacci(4), 4)
print(Solution().tribonacci(25), 1389537)
print(Solution().tribonacci(31), 53798080)
print(Solution().tribonacci(35), 615693474)