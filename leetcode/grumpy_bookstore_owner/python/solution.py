class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: sliding window
        """
        # Total satisfied customers when the bookstore owner is not grumpy.
        satisfied = sum(customer for customer, grump in zip (customers, grumpy) if grump == 0)
        # Satisfied customers within the `minutes` window. Counts only grumpy minumtes.
        window = 0
        max_window = 0
        left = 0

        for right, (customer, grump) in enumerate(zip(customers, grumpy)):
            if grump:
                window += customer

            if right < minutes - 1:
                continue

            max_window = max(max_window, window)

            if grumpy[left]:
                window -= customers[left]
            left += 1

        return satisfied + max_window


print(Solution().maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3) == 16)
print(Solution().maxSatisfied([1], [0], 1) == 1)
print(Solution().maxSatisfied([4, 10, 10], [1, 1, 0], 2) == 24)
