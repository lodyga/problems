import { Deque } from "@datastructures-js/deque";


class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: deque
    *     A: sorting, iteration
    * @param {number[]} deck
    * @return {}
    */
   deckRevealedIncreasing(deck) {
      deck.sort((a, b) => a - b);
      const deq = new Deque(Array.from({ length: deck.length }, (_, index) => index));
      const res = Array(deck.length).fill(0);

      for (const card of deck) {
         res[deq.popFront()] = card;

            if (deq.size())
                deq.pushBack(deq.popFront());
      }

      return res
   };
}


const deckRevealedIncreasing = new Solution().deckRevealedIncreasing;
console.log(new Solution().deckRevealedIncreasing([1, 2, 3, 4, 5]).toString() === [1, 5, 2, 4, 3].toString())
console.log(new Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]).toString() === [2, 13, 3, 11, 5, 17, 7].toString())
console.log(new Solution().deckRevealedIncreasing([1, 1000]).toString() === [1, 1000].toString())
