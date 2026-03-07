class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        from collections import deque
        """
        Time complexity: O(n*m)
            m: tickets[k]
        Auxiliary space complexity: O(n)
        Tags:
            DS: queue
            A: iteration
        """
        res = 0
        queue = deque([(ticket, index)
                      for index, ticket in enumerate(tickets)])

        while True:
            ticket, index = queue.popleft()
            ticket -= 1
            res += 1

            if ticket:
                queue.append((ticket, index))
            elif index == k:
                return res


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        res = 0
        tickets_to_buy = tickets[k]

        for index, ticket in enumerate(tickets):
            if ticket < tickets_to_buy:
                res += ticket
            else:
                res += tickets_to_buy
                res -= 1 if index > k else 0

        return res


print(Solution().timeRequiredToBuy([2, 2], 0) == 3)
print(Solution().timeRequiredToBuy([2, 3, 2], 2) == 6)
print(Solution().timeRequiredToBuy([5, 1, 1, 1], 0) == 8)
