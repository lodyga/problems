class Solution:
    def new21Game(self, upper_point_bound: int, draw_point_limit: int, max_pts: int) -> float:
        """
        Time complexity: O(n2)
            O(max_pts * draw_point_limit)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: top-down
        """
        # The probability that Alice has upper_point_bound or fewer score
        # after drawing a card if she had `draw_point_limit` or less score;
        memo = [-1.0] * (draw_point_limit + 1)

        def dfs(score):
            if score >= draw_point_limit:
                return 1 if score <= upper_point_bound else 0
            elif memo[score] != -1:
                return memo[score]

            points = 0
            for point in range(1, max_pts + 1):
                points += dfs(score + point)

            # The probability of reaching a valid score.
            memo[score] = points / max_pts
            return memo[score]

        return dfs(0)


print(round(Solution().new21Game(10, 1, 10), 5) == 1)
print(round(Solution().new21Game(6, 1, 10), 5) == 0.6)
print(round(Solution().new21Game(2, 2, 10), 5) == 0.11)
print(round(Solution().new21Game(3, 2, 3), 5) == 0.88889)
print(round(Solution().new21Game(21, 17, 10), 5) == 0.73278)
print(round(Solution().new21Game(0, 0, 1), 5) == 1)
print(round(Solution().new21Game(421, 400, 47), 5) == 0.71188)
print(round(Solution().new21Game(9811, 8776, 1096), 5) == 0.99696)


class Solution:
    def new21Game(self, upper_point_bound: int, draw_point_limit: int, max_pts: int) -> float:
        """
        Time complexity: O(2^n)
            O(max_pts ^ draw_point_limit)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force
        """
        def dfs(score):
            if score >= draw_point_limit:
                return score <= upper_point_bound

            occurrence = 0
            for points in range(1, max_pts + 1):
                occurrence += dfs(score + points)
            return occurrence / max_pts

        return dfs(0)


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
