class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: greedy
        """
        price1 = 101
        price2 = 101

        for price in prices:
            if price < price1:
                price2 = price1
                price1 = price
            elif price < price2:
                price2 = price
            
        rest = money - price1 - price2
        return rest if rest >= 0 else money


import heapq


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: heap
            A: iteration
        """
        chocks = []
        for price in prices:
            if len(chocks) < 2:
                heapq.heappush(chocks, -price)
            else:
                heapq.heappushpop(chocks, -price)

        change = money + chocks[0] + chocks[1]
        return change if change >= 0 else money


print(Solution().buyChoco([1, 2, 2], 3) == 0)
print(Solution().buyChoco([3, 2, 3], 3) == 3)
