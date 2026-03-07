class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: intervals
        """
        prev_end = customers[0][0]
        total_wait = 0

        for start, prepare in customers:
            end = max(prev_end, start) + prepare
            total_wait += end - start
            prev_end = end

        return total_wait / len(customers)


print(Solution().averageWaitingTime([[1, 2], [2, 5], [4, 3]]) == 5)
print(Solution().averageWaitingTime([[5, 2], [5, 4], [10, 3], [20, 1]]) == 3.25)
