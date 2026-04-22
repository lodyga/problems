class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        """
        Time complexity: O(qlogm)
            q: quantities length
            m: max quantitity
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        low = 1
        high = max(quantities)
        res = high

        while low <= high:
            mid = (low + high) // 2
            count_shops = 0

            for q in quantities:
                count_shops += ((q - 1) // mid) + 1
                if count_shops > n:
                    break

            if count_shops > n:
                low = mid + 1
            else:
                res = mid
                high = mid - 1

        return res


print(Solution().minimizedMaximum(6, [11, 6]) == 3)
print(Solution().minimizedMaximum(7, [15, 10, 10]) == 5)
print(Solution().minimizedMaximum(1, [100000]) == 100000)
