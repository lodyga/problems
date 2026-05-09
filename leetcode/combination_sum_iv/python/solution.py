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
        res = 0
        
        def dfs(total: int) -> None:
            nonlocal res
            if total >= target:
                res += total == target
                return
            
            for num in nums:
                if total + num > target:
                    break
                dfs(total + num)
        
        dfs(0)
        return res


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
        def dfs(total: int) -> int:
            if total >= target:
                return total == target

            return sum(
                dfs(total + num) 
                for num in nums
            )

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
        # differente from target: number of ways to make `differente from target`
        memo = {target: 1}
        
        def dfs(total: int) -> int:
            if total > target:
                return 0
            elif total in memo:
                return memo[total]
            
            res = sum(
                dfs(total + num)
                for num in nums
            )
            memo[total] = res
            return res

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
        memo = [-1] * target
        memo.append(1)

        def dfs(total: int) -> int:
            if total > target:
                return 0
            elif memo[total] != -1:
                return memo[total]
            
            res = sum(
                dfs(total + num)
                for num in nums
            )
            memo[total] = res
            return res

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
            A: bottom-up
        """
        # The number of ways to make `idx` sum.
        cache = [0] * target
        cache.append(1)

        for idx in range(target - 1, -1, -1):
            for num in nums:
                if idx + num <= target:
                    cache[idx] += cache[idx + num]

        return cache[0]


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n*t)
            n: numbers length
            t: target
        Auxiliary space complexity: O(t)
        Tags:
            DS: array
            A: bottom-up
        """
        # The number of ways to make `idx` sum.
        cache = [0] * (target + 1)
        cache[0] = 1

        for idx in range(1, target + 1):
            for num in nums:
                if idx - num >= 0:
                    cache[idx] += cache[idx - num]

        return cache[-1]


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
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
            for number in nums:
                cache[index] += cache.get(index - number, 0)

        return cache.get(target, 0)


print(Solution().combinationSum4([5], 5) == 1)
print(Solution().combinationSum4([2, 3], 7) == 3)
print(Solution().combinationSum4([1, 2, 3], 4) == 7)
print(Solution().combinationSum4([9], 3) == 0)
print(Solution().combinationSum4([4, 2, 1], 32) == 39882198)
