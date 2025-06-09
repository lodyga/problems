class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags: binary search
    * @param {number[]} spells
    * @param {number[]} potions
    * @param {number} success
    * @return {number[]}
    */
   successfulPairs(spells, potions, success) {
      potions.sort((a, b) => a - b);
      const successfulSpells = Array(spells.length).fill(0);

      for (let index = 0; index < spells.length; index++) {
         const spell = spells[index];
         let left = 0;
         let right = potions.length - 1;

         while (left <= right) {
            const middle = (left + right) >> 1;

            if (potions[middle] * spell >= success) {
               right = middle - 1;
            } else {
               left = middle + 1;
            }
         }
         successfulSpells[index] = potions.length - left;
      }
      return successfulSpells
   };
}
const successfulPairs = new Solution().successfulPairs;


console.log(new Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7), [4, 0, 3])
console.log(new Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16), [2, 0, 2])
console.log(new Solution().successfulPairs([39, 34, 6, 35, 18, 24, 40], [27, 37, 33, 34, 14, 7, 23, 12, 22, 37], 43), [10, 10, 9, 10, 10, 10, 10])