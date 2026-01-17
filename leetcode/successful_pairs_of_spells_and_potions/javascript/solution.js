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
      const successfulSpells = Array(spells.length).fill(0);

      for (let index = 0; index < spells.length; index++) {
         const spell = spells[index];
         let left = 0;
         let right = potions.length - 1;
         let minRight = potions.length;

         while (left <= right) {
            const middle = (left + right) >> 1;
1
            if (potions[middle] * spell < success) {
               left = middle + 1;
            } else {
               minRight = middle;
               right = middle - 1;
            }
         }
         successfulSpells[index] = potions.length - minRight;
      }
      return successfulSpells
   };
}


const successfulPairs = new Solution().successfulPairs;
console.log(JSON.stringify(new Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7)) === JSON.stringify([4, 0, 3]))
console.log(JSON.stringify(new Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16)) === JSON.stringify([2, 0, 2]))
console.log(JSON.stringify(new Solution().successfulPairs([39, 34, 6, 35, 18, 24, 40], [27, 37, 33, 34, 14, 7, 23, 12, 22, 37], 43)) === JSON.stringify([10, 10, 9, 10, 10, 10, 10]))
