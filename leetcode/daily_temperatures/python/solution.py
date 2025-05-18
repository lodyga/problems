class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack, monotonic stack
        monotonically decreasing stack
        """
        # [(day, temperature), ]
        temperature_stack = []
        # number of days needed to wait after day ith for a warmer day to arrive
        days_to_get_warmer = [0] * len(temperatures)

        for day, temperature in enumerate(temperatures):
            while temperature_stack and temperature_stack[-1][1] < temperature:
                prev_day, _ = temperature_stack.pop()
                days_to_get_warmer[prev_day] = day - prev_day
            
            temperature_stack.append((day, temperature))
        
        return days_to_get_warmer


class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        days_to_get_warmer = [0] * len(temps)

        for left in range(len(temps)):
            for right in range(left + 1, len(temps)):
                if temps[left] < temps[right]:
                    days_to_get_warmer[left] = right - left
                    break
        
        return days_to_get_warmer


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0])
print(Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0])
print(Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0])