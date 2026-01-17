class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: hash map
    *     A: sorting
    * @param {number[]} hand
    * @param {number} groupSize
    * @return {boolean}
    */
   isNStraightHand(hand, groupSize) {
      if (hand.length % groupSize) {
         return false
      }

      hand.sort((a, b) => a - b);
      const cardFreq = new Map();

      for (const card of hand) {
         cardFreq.set(card, (cardFreq.get(card) || 0) + 1)
      }

      for (const headCard of hand) {
         if (!cardFreq.has(headCard)) {
            continue
         }

         for (let card = headCard; card < headCard + groupSize; card++) {
            if (!cardFreq.has(card)) {
               return false
            }
            cardFreq.set(card, cardFreq.get(card) - 1);
            if (cardFreq.get(card) === 0) {
               cardFreq.delete(card);
            }
         }
      }
      return true
   };
}


const isNStraightHand = new Solution().isNStraightHand;
console.log(new Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) === true)
console.log(new Solution().isNStraightHand([1, 2, 3, 4, 5], 4) === false)
console.log(new Solution().isNStraightHand([1], 1) === true)
console.log(new Solution().isNStraightHand([5, 1, 0, 6, 4, 5, 3, 0, 8, 9], 2) === false)
console.log(new Solution().isNStraightHand([9, 13, 15, 23, 22, 25, 4, 4, 29, 15, 8, 23, 12, 19, 24, 17, 18, 11, 22, 24, 17, 17, 10, 23, 21, 18, 14, 18, 7, 6, 3, 6, 19, 11, 16, 11, 12, 13, 8, 26, 17, 20, 13, 19, 22, 21, 27, 9, 20, 15, 20, 27, 8, 13, 25, 23, 22, 15, 9, 14, 20, 10, 6, 5, 14, 12, 7, 16, 21, 18, 21, 24, 23, 10, 21, 16, 18, 16, 18, 5, 20, 19, 20, 10, 14, 26, 2, 9, 19, 12, 28, 17, 5, 7, 25, 22, 16, 17, 21, 11], 10) === false)
