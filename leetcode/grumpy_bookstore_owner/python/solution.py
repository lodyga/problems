class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: sliding window
        """
        if len(grumpy) <= minutes:
            return sum(customers)

        # satisfied customers within the window
        window = 0
        # the rest of satisfied customers (not within the window)
        outside_window = sum(customers[index] for index in range(len(customers)) if grumpy[index] == 0)
        max_customers = 0
        left = 0

        for right, customer in enumerate(customers):
            window += customer
            # remove customers added to the window from `outside of the window`
            outside_window -= customer if grumpy[right] == 0 else 0

            if right - left + 1 < minutes:
                continue
            
            max_customers = max(max_customers, window + outside_window)
            left_customer = customers[left]
            window -= left_customer
            # add customers to `outside of the window`
            outside_window += left_customer if grumpy[left] == 0 else 0
            left += 1

        return max_customers


class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: sliding window
        """
        # satisfied customers only from grumpy ones within the window
        window = 0
        max_window = 0
        # all of the satisfied customers
        satisfied = 0
        left = 0

        for right, customer in enumerate(customers):
            if grumpy[right]:
                window += customer
            else:
                satisfied += customer

            if right - left + 1 < minutes:
                continue
            
            max_window = max(max_window, window)
            if grumpy[left]:
                window -= customers[left]
            left += 1

        return satisfied + max_window


print(Solution().maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3) == 16)
print(Solution().maxSatisfied([1], [0], 1) == 1)
print(Solution().maxSatisfied([4, 10, 10], [1, 1, 0], 2) == 24)