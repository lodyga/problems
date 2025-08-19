class Solution:
    def new21Game(self, upper_bound: int, threshold: int, maxPts: int) -> float:
        """
        Time complexity: O(n2)
            O(maxPts*threshold)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        # the probability that Alice has upper_bound or fewer score after drawing a card if she had `threshold` or less score
        memo = {}

        def dfs(score):
            if score in memo:
                return memo[score]
            elif score >= threshold:
                return score <= upper_bound

            # is the number of valid outcomes (paths) from the current state.
            occurrence = 0
            for points in range(1, maxPts + 1):
                occurrence += dfs(score + points)
            
            # is the probability of reaching a valid score from the current state.
            memo[score] = occurrence / maxPts
            return memo[score]

        return dfs(0)


class Solution:
    def new21Game(self, upper_bound: int, threshold: int, maxPts: int) -> float:
        """
        Time complexity: O(2^n)
            O(maxPts^threshold)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(score):
            if score >= threshold:
                return score <= upper_bound

            occurrence = 0
            for points in range(1, maxPts + 1):
                occurrence += dfs(score + points)
            return occurrence / maxPts

        return dfs(0)


print(Solution().new21Game(10, 1, 10), 1)
print(Solution().new21Game(6, 1, 10), 0.6)
print(Solution().new21Game(2, 2, 10), 0.11)
print(Solution().new21Game(3, 2, 3), 0.88889)
print(Solution().new21Game(21, 17, 10), 0.73278)
print(Solution().new21Game(421, 400, 47), 0.71188)  # tle
print(Solution().new21Game(9811, 8776, 1096), 0.99670)  # tle


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0

        windowSum = sum(
            i <= n 
            for i in range(k, k + maxPts))
        
        dp = {}
        for i in range(k - 1, -1, -1):
            dp[i] = windowSum / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1)
            
            windowSum += dp[i] - remove
        
        return dp[0]