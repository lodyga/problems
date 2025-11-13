class Solution:
    def totalMoney(self, days: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        weeks = days // 7
        left = days % 7
        total = 0

        for week in range(weeks):
            total += ((1 + 7 + 2*week) * 7 // 2)

        last_week = weeks + 1
        total += (last_week + (last_week + left - 1)) * left // 2

        return total


class Solution:
    def totalMoney(self, days: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        weeks = days // 7
        left = days % 7
        total = sum(((1 + 7 + 2*week) * 7 // 2) for week in range(weeks))

        last_week = weeks + 1
        total += (last_week + (last_week + left - 1)) * left // 2

        return total


print(Solution().totalMoney(4) == 10)
print(Solution().totalMoney(10) == 37)
print(Solution().totalMoney(20) == 96)
