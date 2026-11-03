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
        def dfs(total: int) -> None:
            nonlocal res

            if total >= target:
                res += total == target
                return

            for num in nums:
                if total + num > target:
                    break
                dfs(total + num)

        nums.sort()
        res = 0
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

        # differente from target: number of ways to make `differente from target`
        memo = {target: 1}
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

        # The number of ways to make `current` sum.
        memo = [-1] * target
        memo.append(1)
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
        # The number of ways to make `idx` sum.
        cache = {0: 1}

        for idx in range(1, target + 1):
            cache[idx] = 0

            for num in nums:
                cache[idx] += cache.get(idx - num, 0)

        return cache.get(target, 0)


print(Solution().combinationSum4([1, 2, 3], 4) == 7)
print(Solution().combinationSum4([9], 3) == 0)
print(Solution().combinationSum4([5], 5) == 1)
print(Solution().combinationSum4([2, 3], 7) == 3)
print(Solution().combinationSum4([4, 2, 1], 32) == 39882198)
print(Solution().combinationSum4([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 111], 999))
