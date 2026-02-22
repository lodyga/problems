class Solution:
    def totalMoney(self, days: int) -> int:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags:
            A: math, iteration
            Arithmetic series
        """
        weeks = days // 7
        last_week_days = days % 7
        whole_weeks_money_sum = 0

        for week in range(1, weeks + 1):
            whole_weeks_money_sum += (week + (week - 1 + 7)) * 7 // 2

        last_week_money_sum = (
            (weeks + 1) +
            (weeks + last_week_days)
        ) * last_week_days // 2

        return whole_weeks_money_sum + last_week_money_sum


print(Solution().totalMoney(4) == 10)
print(Solution().totalMoney(10) == 37)
print(Solution().totalMoney(20) == 96)
