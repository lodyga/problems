class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            A: bottom-up
        """
        # Champagne going through i-th glass in current row.
        prev_cache = [poured]

        for row in range(1, query_row + 1):
            cache = [0] * (row + 1)

            for col in range(row):
                side_spill = (prev_cache[col] - 1) / 2
                if side_spill > 0:
                    cache[col] += side_spill
                    cache[col + 1] += side_spill

            prev_cache = cache

        return min(1, prev_cache[query_glass])


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            A: bottom-up
        """
        # champagne going through i-th glass on current row
        prev_cache = [poured]

        for row in range(query_row):
            cache = [0] * (row + 2)

            for col, champ in enumerate(prev_cache):
                if champ >= 1:
                    champ = (champ - 1) / 2
                    cache[col] += champ
                    cache[col + 1] += champ

            prev_cache = cache

        return min(1, prev_cache[query_glass])


print(Solution().champagneTower(1, 1, 1) == 0)
print(Solution().champagneTower(2, 1, 1) == 0.5)
print(Solution().champagneTower(4, 2, 0) == 0.25)
print(Solution().champagneTower(4, 2, 1) == 0.5)
print(Solution().champagneTower(100000009, 33, 17) == 1)
print(Solution().champagneTower(0, 0, 0) == 0)
print(Solution().champagneTower(25, 6, 1) == 0.18750)


# tower = [[1], [[1], [1]], [[0.25], [0.5], [0.5]]]
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Failed attempt.
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: bottom-up
        """
        for row in range(query_row):
            poured -= (row + 1)

            if poured <= row + 2:
                side_spill = poured / (row + 1) / 2
                if query_glass in (0, row + 1):
                    return side_spill
                else:
                    return side_spill * 2
                # tower = [side_spill * 2 for _ in range(row)]
                # tower.insert(0, side_spill)
                # tower.append(side_spill)
                return tower[query_glass]

        return 1
