class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        # champagne going through i-th glass on current row
        cache = [poured]  

        for row in range(query_row):
            next_cache = [0] * (row + 2)
            
            for col, champ in enumerate(cache):
                if champ >= 1:
                    champ = (champ - 1) / 2
                    next_cache[col] += champ
                    next_cache[col + 1] += champ

            cache = next_cache
        
        return min(1, cache[query_glass])


print(Solution().champagneTower(1, 1, 1) == 0)
print(Solution().champagneTower(2, 1, 1) == 0.5)
print(Solution().champagneTower(4, 2, 0) == 0.25)
print(Solution().champagneTower(4, 2, 1) == 0.5)
print(Solution().champagneTower(100000009, 33, 17) == 1)