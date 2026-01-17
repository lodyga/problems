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


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: greedy
        """
        chocks = [101, 101]
        for price in prices:
            if price < chocks[0]:
                chocks[1] = chocks[0]
                chocks[0] = price
            elif price < chocks[1]:
                chocks[1] = price
        
        change = money - chocks[0] - chocks[1]
        return change if change >= 0 else money


print(Solution().buyChoco([1, 2, 2], 3) == 0)
print(Solution().buyChoco([3, 2, 3], 3) == 3)
