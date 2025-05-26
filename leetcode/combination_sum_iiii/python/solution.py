class Solution:
    def combinationSum4(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(n*t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags: dp, top-down with memoization as list
        """
        # The number of ways to make `current` sum.
        memo = [None] * (target + 1)
        memo[-1] = 1

        def dfs(current: int) -> int:
            if current >= len(memo):
                return 0
            elif memo[current] is not None:
                return memo[current]
            else:
                memo[current] = sum(dfs(current + numbers[index])
                                    for index in range(len(numbers)))
                return memo[current]

        dfs(0)
        return memo[0]


class Solution:
    def combinationSum4(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(n*t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags: dp, top-down with memoization as hash map
        """
        # The number of ways to make `current` sum.
        memo = {target: 1}

        def dfs(current: int) -> int:
            if current > target:
                return 0
            elif current in memo:
                return memo[current]
            else:
                memo[current] = sum(dfs(current + numbers[index])
                                    for index in range(len(numbers)))
                return memo[current]

        dfs(0)
        return memo[0]


class Solution:
    def combinationSum4(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(n*t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags: dp, bottom-up with tabulation as list
        """
        # The number of ways to make `index` sum.
        cache = [0] * (target + 1)
        cache[0] = 1

        for index in range(1, target + 1):
            for number in numbers:
                if index - number >= 0:
                    cache[index] += cache[index - number]

        return cache[-1]


class Solution:
    def combinationSum4(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(n*t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags: dp, bottom-up with tabulation as hash map
        """
        # The number of ways to make `index` sum.
        cache = {0: 1}

        for index in range(1, target + 1):
            for number in numbers:
                cache[index] = (cache.get(index, 0) + 
                                    cache.get(index - number, 0))

        return cache.get(target, 0)


class Solution:
    def combinationSum4(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(2^n)
            O(n^t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags: brute force, backtracking, tle
        pure function, converts to top-down
        """
        def dfs(current: int) -> int:
            if current > target:
                return 0
            elif current == target:
                return 1
            else:
                return sum(dfs(current + numbers[index])
                                    for index in range(len(numbers)))

        return dfs(0)


class Solution:
    def combinationSum4(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(2^n)
            O(n^t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags: brute force, backtracking, tle
        side effect
        """
        self.combination_count = 0

        def dfs(target: int) -> None:
            if target == 0:
                self.combination_count += 1
                return
            elif target < 0:
                return

            for index in range(len(numbers)):
                dfs(target - numbers[index])

        dfs(target)
        return self.combination_count


print(Solution().combinationSum4([5], 5) == 1)
print(Solution().combinationSum4([2, 3], 7) == 3)
print(Solution().combinationSum4([1, 2, 3], 4) == 7)
print(Solution().combinationSum4([9], 3) == 0)
print(Solution().combinationSum4([4, 2, 1], 32) == 39882198)