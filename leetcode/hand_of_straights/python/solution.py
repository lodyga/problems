class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sorting
        """
        if len(hand) % groupSize:
            return False
        
        hand.sort()
        
        card_frequency = {}
        for card in hand:
            if card not in card_frequency:
                card_frequency[card] = 0
            card_frequency[card] = card_frequency.get(card, 0) + 1

        for base_card in hand:
            if base_card not in card_frequency:
                continue
            
            for card in range(base_card, base_card + groupSize):
                if card in card_frequency:
                    card_frequency[card] -= 1
                    if card_frequency[card] == 0:
                        del card_frequency[card]
                else:
                    return False

        return True


import heapq


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sorting, heap
        """
        if len(hand) % groupSize:
            return False
        
        heapq.heapify(hand)
        
        card_frequency = {}
        for card in hand:
            if card not in card_frequency:
                card_frequency[card] = 0
            card_frequency[card] = card_frequency.get(card, 0) + 1

        while hand:
            base_card = heapq.heappop(hand)
            if base_card not in card_frequency:
                continue
            
            for card in range(base_card, base_card + groupSize):
                if card in card_frequency:
                    card_frequency[card] -= 1
                    if card_frequency[card] == 0:
                        del card_frequency[card]
                else:
                    return False

        return True


print(Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True)
print(Solution().isNStraightHand([1, 2, 3, 4, 5], 4), False)
print(Solution().isNStraightHand([1], 1), True)