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
      let minBananaPerHour = right;

      while (left <= right) {
         const middle = (left + right) >> 1;
         let timeToEat = 0;
         for (const pile of piles) {
            timeToEat += Math.ceil(pile / middle)
            if (timeToEat > hours)
               break
         }

         if (timeToEat <= hours) {
            minBananaPerHour = middle;
            right = middle - 1;
         } else {
            left = middle + 1;
         }
      }
      return minBananaPerHour
   };
}


const minEatingSpeed = new Solution().minEatingSpeed;
console.log(new Solution().minEatingSpeed([3, 6, 7, 11], 8) === 4)
console.log(new Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) === 30)
console.log(new Solution().minEatingSpeed([30, 11, 23, 4, 20], 6) === 23)
console.log(new Solution().minEatingSpeed([312884470], 312884469) === 2)
console.log(new Solution().minEatingSpeed([3], 2) === 2)