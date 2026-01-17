class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(2^n)
            O(n^t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags:
            A: brute-force
        side effect
        """
        nums.sort()
        counter = 0
        
        def dfs(total: int) -> None:
            nonlocal counter
            if total >= target:
                counter += total == target
                return
            
            for num in nums:
                if total + num > target:
                    break
                dfs(total + num)
        
        dfs(0)
        return counter


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(2^n)
            O(n^t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags:
            A: brute-force
        pure function, converts to top-down
        """
        def dfs(current: int) -> int:
            if current >= target:
                return current == target

            return sum(dfs(current + num) 
                       for num in nums)

        return dfs(0)


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n*t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags:
            DS: hash map
            A: top-down
        """
        # current sum: number of ways to make `current sum`
        memo = {target: 1}

        def dfs(current: int) -> int:
            if current > target:
                return 0
            elif current in memo:
                return memo[current]

            memo[current] = 0 
            for num in nums:
                memo[current] += dfs(current + num)

            return memo[current]

        return dfs(0)


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n*t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags:
            DS: array
            A: top-down
        """
        # The number of ways to make `current` sum.
        memo = [-1] * (target + 1)
        memo[-1] = 1

        def dfs(current: int) -> int:
            if current > target:
                return 0
            elif memo[current] != -1:
                return memo[current]
            
            memo[current] = 0
            for num in nums:
                memo[current] += dfs(current + num)

            return memo[current]

        return dfs(0)


class Solution:
    def combinationSum4(self, numbers: list[int], target: int) -> int:
        """
        Time complexity: O(n*t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags:
            DS: array
            A: bottom-up
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
        Tags:
            DS: hash map
            A: bottom-up
        """
        # The number of ways to make `index` sum.
        cache = {0: 1}

        for index in range(1, target + 1):
            cache[index] = 0
            for number in numbers:
                cache[index] += cache.get(index - number, 0)

        return cache.get(target, 0)


print(Solution().combinationSum4([5], 5) == 1)
print(Solution().combinationSum4([2, 3], 7) == 3)
print(Solution().combinationSum4([1, 2, 3], 4) == 7)
print(Solution().combinationSum4([9], 3) == 0)
print(Solution().combinationSum4([4, 2, 1], 32) == 39882198)
