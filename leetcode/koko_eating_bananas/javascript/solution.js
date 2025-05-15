class Solution {
   /**
    * Time complexity: O(nlogm)
    *     n: pile length 
    *     m: highest pile stack
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} piles
    * @param {number} houns
    * @return {number}
    */
   minEatingSpeed(piles, hours) {
      let left = 1;
      let right = Math.max(...piles);

      while (left < right) {
         const middle = (left + right) >> 1;
         const timeToEat = piles.reduce((sum, value) => sum + Math.ceil(value / middle), 0);

         if (timeToEat < hours) {
            right = middle;
         } else {
            left = middle + 1;
         }
      }
      return right
   };
}


console.log(new Solution().minEatingSpeed([3, 6, 7, 11], 8), 4)
console.log(new Solution().minEatingSpeed([30, 11, 23, 4, 20], 5), 30)
console.log(new Solution().minEatingSpeed([30, 11, 23, 4, 20], 6), 23)
console.log(new Solution().minEatingSpeed([312884470], 312884469), 2)
console.log(new Solution().minEatingSpeed([3], 2), 2)