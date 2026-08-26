class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        """
        Time complexity: O(n*m)
            n: stone count
            m: stone sum
        Auxiliary space complexity: O(n*m)
        Tags:
            DS: hash map
            A: top-down
        """
        def dfs(idx: int, total: int) -> int:
            key = (idx, total)
            if (
                total >= half or 
                idx == len(stones)
            ):
                # Returns the difference between both part sums.
                return abs(total - (stone_sum - total))
            elif key in memo:
                return memo[key]

            stone = stones[idx]
            skip = dfs(idx + 1, total)
            take = dfs(idx + 1, stone + total)
            res = min(skip, take)
            memo[key] = res
            return res

        stone_sum = sum(stones)
        half = stone_sum // 2
        memo = {}
        return dfs(0, 0)


print(Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1)
print(Solution().lastStoneWeightII([31, 26, 33, 21, 40]) == 5)
print(Solution().lastStoneWeightII([3, 3]) == 0)
