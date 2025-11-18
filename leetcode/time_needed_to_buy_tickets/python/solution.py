from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        """
        Time complexity: O(nm)
            m: position k tickets
        Auxiliary space complexity: O(n)
        Tags: queue
        """
        queue = deque(
            [(person, ticket)
             for person, ticket in enumerate(tickets)]
        )
        time = 0
        while True:
            person, ticket = queue.popleft()
            ticket -= 1
            time += 1
            if ticket != 0:
                queue.append((person, ticket))
            elif person == k:
                return time


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        """
        time = 0
        tickets_to_buy = tickets[k]

        for index, ticket in enumerate(tickets):
            if index <= k:
                time += min(ticket, tickets_to_buy)
            else:
                time += min(ticket, tickets_to_buy - 1)

        return time


print(Solution().timeRequiredToBuy([2, 2], 0) == 3)
print(Solution().timeRequiredToBuy([2, 3, 2], 2) == 6)
print(Solution().timeRequiredToBuy([5, 1, 1, 1], 0) == 8)
