class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        penalty = customers.count("Y")
        close = (penalty, 0)

        for index, customer in enumerate(customers):
            if customer == "Y":
                penalty -= 1
                if penalty < close[0]:
                    close = (penalty, index + 1)
            else:
                penalty += 1
        
        return close[1]


print(Solution().bestClosingTime("YYNY") == 2)
print(Solution().bestClosingTime("NNNNN") == 0)
print(Solution().bestClosingTime("YYYY") == 4)