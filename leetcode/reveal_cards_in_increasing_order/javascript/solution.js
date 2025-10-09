import { Queue } from "@datastructures-js/queue";


class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: queue
    * @param {number[]} deck
    * @return {}
    */
   deckRevealedIncreasing(deck) {
      deck.sort((a, b) => b - a);
      const queue = new Queue();
      for (const card of deck) {
         queue.enqueue(card);
         if (
            queue.size() > 1 &&
            queue.size() < deck.length
         )
            queue.enqueue(queue.pop())
      }
      return queue.toArray().reverse();
   };
}


const deckRevealedIncreasing = new Solution().deckRevealedIncreasing;
console.log(new Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]), [2, 13, 3, 11, 5, 17, 7])
console.log(new Solution().deckRevealedIncreasing([1, 1000]), [1, 1000])