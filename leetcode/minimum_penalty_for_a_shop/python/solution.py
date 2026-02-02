class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: greedy, prefix sum
        """
        # "Y" postfix sum
        y_postfix = customers.count("Y")
        # "N" prefix sum
        n_prefix = 0
        penalties = [y_postfix]

        for customer in customers:
            if customer == "Y":
                y_postfix -= 1
            else:
                n_prefix += 1
            
            penalties.append(y_postfix + n_prefix)

        min_penalty = penalties[0]
        closing_hour = 0

        for hour, penalty in enumerate(penalties):
            if penalty < min_penalty:
                min_penalty = penalty
                closing_hour = hour

        return closing_hour


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, prefix sum
        """
        # "Y" postfix sum
        y_postfix = customers.count("Y")
        # "N" prefix sum
        n_prefix = 0
        min_penalty = y_postfix
        closing_hour = 0

        for hour, customer in enumerate(customers, 1):
            if customer == "Y":
                y_postfix -= 1
            else:
                n_prefix += 1
            
            penalty = y_postfix + n_prefix
            
            if penalty < min_penalty:
                min_penalty = penalty
                closing_hour = hour

        return closing_hour


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, prefix sum
        """
        # "Y" postfix sum - "N" prefix sum
        penalty = customers.count("Y")
        min_penalty = penalty
        closing_hour = 0

        for hour, customer in enumerate(customers, 1):
            penalty += -1 if customer == "Y" else 1
            
            if penalty < min_penalty:
                min_penalty = penalty
                closing_hour = hour

        return closing_hour


print(Solution().bestClosingTime("YYNY") == 2)
print(Solution().bestClosingTime("NNNNN") == 0)
print(Solution().bestClosingTime("YYYY") == 4)
