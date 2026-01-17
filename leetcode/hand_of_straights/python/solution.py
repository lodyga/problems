import heapq


class Solution:
    def isNStraightHand(self, hand: list[int], group_size: int) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap, hash map
            A: iteration
        """
        if len(hand) % group_size:
            return False

        card_freq = {}
        for num in hand:
            card_freq[num] = card_freq.get(num, 0) + 1

        card_heap = []
        for num in card_freq:
            heapq.heappush(card_heap, num)

        while card_freq:
            while card_heap[0] not in card_freq:
                heapq.heappop(card_heap)

            head_card = card_heap[0]
            for card in range(head_card, head_card + group_size):
                if card not in card_freq:
                    return False
                
                card_freq[card] -= 1
                if card_freq[card] == 0:
                    card_freq.pop(card)

        return True


class Solution:
    def isNStraightHand(self, hand: list[int], group_size: int) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: sorting
        """
        if len(hand) % group_size:
            return False
        
        hand.sort()
        
        card_freq = {}
        for card in hand:
            card_freq[card] = card_freq.get(card, 0) + 1

        for head_card in hand:
            if head_card not in card_freq:
                continue
            
            for card in range(head_card, head_card + group_size):
                if card not in card_freq:
                    return False

                card_freq[card] -= 1
                if card_freq[card] == 0:
                    card_freq.pop(card)

        return True


print(Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) == True)
print(Solution().isNStraightHand([1, 2, 3, 4, 5], 4) == False)
print(Solution().isNStraightHand([1], 1) == True)
print(Solution().isNStraightHand([5, 1, 0, 6, 4, 5, 3, 0, 8, 9], 2) == False)
print(Solution().isNStraightHand([9, 13, 15, 23, 22, 25, 4, 4, 29, 15, 8, 23, 12, 19, 24, 17, 18, 11, 22, 24, 17, 17, 10, 23, 21, 18, 14, 18, 7, 6, 3, 6, 19, 11, 16, 11, 12, 13, 8, 26, 17, 20, 13, 19, 22, 21, 27, 9, 20, 15, 20, 27, 8, 13, 25, 23, 22, 15, 9, 14, 20, 10, 6, 5, 14, 12, 7, 16, 21, 18, 21, 24, 23, 10, 21, 16, 18, 16, 18, 5, 20, 19, 20, 10, 14, 26, 2, 9, 19, 12, 28, 17, 5, 7, 25, 22, 16, 17, 21, 11], 10) == False)
