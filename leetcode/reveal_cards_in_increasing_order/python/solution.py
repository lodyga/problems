class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        from collections import deque
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: deque
            A: sorting, iteration
        """
        N = len(deck)
        deck.sort()
        deq = deque(range(N))
        res = [0] * N

        for card in deck:
            res[deq.popleft()] = card
            if deq:
                deq.append(deq.popleft())

        return res


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: sorting, iteration
        """
        def get_next_avaible_index(index):
            index += 1
            while res[index % N] != 0:
                index += 1
            return index
            
        N = len(deck)
        deck.sort()
        res = [0] * N
        res_index = 0

        for index in range(N - 1):
            res[res_index % N] = deck[index]

            # next index to skip
            res_index = get_next_avaible_index(res_index)
            # next index to fill
            res_index = get_next_avaible_index(res_index)

        for index, num in enumerate(res):
            if num == 0:
                res[index] = deck[-1]
        
        return res


print(Solution().deckRevealedIncreasing([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3])
print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]) == [2, 13, 3, 11, 5, 17, 7])
print(Solution().deckRevealedIncreasing([1, 1000]) == [1, 1000])
