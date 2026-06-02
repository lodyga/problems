class Solution {
   /**
    * Time complexity: O(mlogm + nlogm)
    *     n: spell count 
    *     m: potion count
    * Auxiliary space complexity: O(n + m)
    * Tags:
    *     DS: array
    *     A: binary search, sorting
    * @param {number[]} spells
    * @param {number[]} potions
    * @param {number} success
    * @return {number[]}
    */
   successfulPairs(spells, potions, success) {
      potions.sort((a, b) => a - b);
      const res = []

      for (let ids = 0; ids < spells.length; ids++) {
         const spell = spells[ids];
         let left = 0;
         let right = potions.length - 1;
         let failCounter = potions.length;
         const potionThreshold = success / spell;

         while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            const midPotion = potions[mid];

            if (midPotion < potionThreshold) {
               left = mid + 1;
            } else {
               failCounter = mid;
               right = mid - 1;
            }
         }

         res.push(potions.length - failCounter);
      }

      return res;
   }
}


const successfulPairs = new Solution().successfulPairs;
console.log(JSON.stringify(new Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7)) === JSON.stringify([4, 0, 3]))
console.log(JSON.stringify(new Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16)) === JSON.stringify([2, 0, 2]))
console.log(JSON.stringify(new Solution().successfulPairs([39, 34, 6, 35, 18, 24, 40], [27, 37, 33, 34, 14, 7, 23, 12, 22, 37], 43)) === JSON.stringify([10, 10, 9, 10, 10, 10, 10]))
