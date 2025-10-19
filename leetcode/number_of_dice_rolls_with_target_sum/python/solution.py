class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        Time complexity: O(n3)
            O(n*t*k)
            n: dice count
            t: target
            k: die face count
        Auxiliary space complexity: O(n2)
            O(n*t)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {(rolled dice counter, accumulated): count ways to target with dice left}
        MOD = 10**9 + 7
        
        def dfs(dice, total):
            if dice == n:
                return total == target
            elif total >= target:
                return 0
            elif (dice, total) in memo:
                return memo[(dice, total)]
            
            memo[(dice, total)] = 0
            for face in range(1, k + 1):
                memo[(dice, total)] += dfs(dice + 1, total + face)
            
            memo[(dice, total)] %= MOD
            return memo[(dice, total)]
        
        return dfs(0, 0)


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        Time complexity: O(n3)
            O(n*t*k)
            n: dice count
            t: target
            k: die face count
        Auxiliary space complexity: O(n2)
            O(n*t)
        Tags: dp, top-down with memoization as hash map
        Die count and total accumulates like in bottom-up.
        """
        memo = {}  # {(rolled dice counter, accumulated): count ways to target with dice left}
        MOD = 10**9 + 7
        
        def dfs(dice, target):
            if dice == 0:
                return target == 0
            elif target <= 0:
                return 0
            elif (dice, target) in memo:
                return memo[(dice, target)]
            
            memo[(dice, target)] = 0
            for face in range(1, k + 1):
                memo[(dice, target)] += dfs(dice - 1, target - face)
            
            memo[(dice, target)] %= MOD
            return memo[(dice, target)]
        
        return dfs(n, target)


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        Time complexity: O(n3)
            O(n*t*k)
            n: dice count
            t: target
            k: die face count
        Auxiliary space complexity: O(n2)
            O(n*t)
        Tags: dp, bottom-up
        """
        # Number of ways [i, j] to accumulate with i dices j total
        cache = [[0] * (target + 1) for _ in range(n + 1)]
        cache[0][0] = 1 # one way to get to zero target with zero dice.
        MOD = 10**9 + 7

        for die in range(1, n + 1):
            for face in range(1, k + 1):
                for total in range(face, target + 1):
                    cache[die][total] += cache[die - 1][total - face]
                    cache[die][total] %= MOD

        return cache[-1][target]


print(Solution().numRollsToTarget(1, 6, 3) == 1)
print(Solution().numRollsToTarget(2, 6, 7) == 6)
print(Solution().numRollsToTarget(3, 6, 9) == 25)
print(Solution().numRollsToTarget(30, 30, 500) == 222616187)