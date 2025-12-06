class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: monotonic decreasing stack
            A: iteration
        """
        # decreasing temperature day stack
        day_stack = []
        wait_days = [0] * len(temperatures)
        
        for day, temp in enumerate(temperatures):
            while day_stack and temperatures[day_stack[-1]] < temp:
                prev_day = day_stack.pop()
                wait_days[prev_day] = day - prev_day
            else:
                day_stack.append(day)
        
        return wait_days


class Solution2:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: 
            A: brute-force
        """
        wait_days = [0] * len(temps)

        for left in range(len(temps)):
            for right in range(left + 1, len(temps)):
                if temps[left] < temps[right]:
                    wait_days[left] = right - left
                    break
        
        return wait_days


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0])
print(Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0])
print(Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0])
