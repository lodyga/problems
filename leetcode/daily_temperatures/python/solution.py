class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic decreasing stack
            A: iteration
        """
        res = [0] * len(temps)
        stack = []

        for idx, temp in enumerate(temps):
            while stack and temps[stack[-1]] < temp:
                prev_idx = stack.pop()
                res[prev_idx] = idx - prev_idx

            stack.append(idx)

        return res


class Solution:
    def dailyTemperatures(self, temps: list[int]) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        res = [0] * len(temps)

        for left in range(len(temps)):
            for right in range(left + 1, len(temps)):
                if temps[left] < temps[right]:
                    res[left] = right - left
                    break
        
        return res


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0])
print(Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0])
print(Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0])
