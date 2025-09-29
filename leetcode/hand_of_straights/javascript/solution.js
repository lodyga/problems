class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags: sorting
    * @param {number[]} hand
    * @param {number} groupSize
    * @return {boolean}
    */
   isNStraightHand(hand, groupSize) {
      if (hand.length % groupSize) {
         return false
      }
      const cardFrequency = new Map();
      for (const card of hand) {
         cardFrequency.set(card, (cardFrequency.get(card) || 0) + 1)
      }
      hand.sort((a, b) => a - b);
      
      for (const base_card of hand) {
         if (!cardFrequency.get(base_card)) {
            continue
         }
         for (let index = 0; index < groupSize; index++) {
            const card = base_card + index;
            
            if (cardFrequency.has(card)) {
               cardFrequency.set(card, cardFrequency.get(card) - 1);
               if (cardFrequency.get(card) === 0) {
                  cardFrequency.delete(card);
               }
            } else {
               return false
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