class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        """
        Time complexity: O(n*m)
            n: stone count
            m: stone sum
        Auxiliary space complexity: O(n*m)
        Tags: dp, top-down with memoization as hash map
        """
        total = sum(stones)
        target = (total + 1) // 2
        memo = {}  # {(indext, current_sum: min stone weight)}

        def dfs(index, current_sum):
            if (
                current_sum >= target or 
                index == len(stones)
            ):
                return abs(current_sum - (total - current_sum))
            elif (index, current_sum) in memo:
                return memo[(index, current_sum)]
        
            memo[(index, current_sum)] = min(
                dfs(index + 1, current_sum + stones[index]), 
                dfs(index + 1, current_sum)
            )
            return memo[index, current_sum]

        return dfs(0, 0)


print(Solution().lastStoneWeightII([3, 3]) == 0)
print(Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1)
print(Solution().lastStoneWeightII([31, 26, 33, 21, 40]) == 5)