from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: queue
        """
        queue = deque()
        deck.sort()
        for card in reversed(deck):
            queue.appendleft(card)
            if (
                len(queue) > 1 and 
                len(queue) < len(deck)
            ):
                queue.appendleft(queue.pop())
        return list(queue)


print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]) == [2, 13, 3, 11, 5, 17, 7])
print(Solution().deckRevealedIncreasing([1, 1000]) == [1, 1000])