class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number[]} weights
    * @param {number} days
    * @return {number}
    */
   shipWithinDays(weights, days) {
      let left = Math.max(...weights);
      let right = weights.reduce((sum, number) => sum + number, 0);

      while (left < right) {
         const middleCapacity = (left + right) >> 1;
         let daysNeeded = 1;
         let currentCapacity = middleCapacity;

         for (const weight of weights) {
            currentCapacity -= weight;

            if (currentCapacity <0) {
               daysNeeded++;
               currentCapacity = middleCapacity - weight;
            }
         }
         if (daysNeeded <= days)
            right = middleCapacity;
         else
            left = middleCapacity + 1;
      }
      return right
   };
}
const shipWithinDays = new Solution().shipWithinDays;


console.log(new Solution().shipWithinDays([1, 2, 3, 1, 1], 4) === 3)
console.log(new Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) === 15)
console.log(new Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3) === 6)
console.log(new Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) === 55)
console.log(new Solution().shipWithinDays([3, 3, 3, 3, 3, 3], 2) === 9)


class Solution2 {
   /**
    * O(nlogn), O(1)
    * binary search
    * @param {number[]} weights
    * @param {number} days
    * @return {number}
    */
   shipWithinDays(weights, days) {
      function daysToShip(capacity) {
         let days = 1;
         let currentCapacity = capacity;

         for (const weight of weights) {
            if (currentCapacity - weight < 0) {
               days++;
               currentCapacity = capacity;
            }
            currentCapacity -= weight;
         }
         return days;
      }

      let lowCap = Math.max(...weights);
      let highCap = weights.reduce((total, current) => total + current);

      while (lowCap < highCap) {
         const capacity = (lowCap + highCap) >> 1

         if (daysToShip(capacity) > days) {
            lowCap = capacity + 1;
         } else {
            highCap = capacity;
         }
      }

      return highCap
   };
}