class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: binary search
    * @param {number[]} weights
    * @param {number} days
    * @return {number}
    */
   shipWithinDays(weights, days) {
      const canTransport = (capacity) => {
         const capacityCopy = capacity;
         let transDays = 1;

         for (const weight of weights) {
            if (transDays > days)
               return false

            capacity -= weight;

            if (capacity < 0) {
               transDays += 1;
               capacity = capacityCopy - weight;
            }
         }
         return transDays <= days
      }

      // capacities
      let left = Math.max(...weights);
      let right = weights.reduce((total, num) => total + num, 0);
      let res = weights.length;

      while (left <= right) {
         const mid = (left + right) >> 1;

         if (canTransport(mid)) {
            res = mid;
            right = mid - 1;
         } else
            left = mid + 1;
      }
      return res
   };
}


const shipWithinDays = new Solution().shipWithinDays;
console.log(new Solution().shipWithinDays([1, 2, 3, 1, 1], 4) === 3)
console.log(new Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) === 15)
console.log(new Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3) === 6)
console.log(new Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) === 55)
console.log(new Solution().shipWithinDays([3, 3, 3, 3, 3, 3], 2) === 9)
