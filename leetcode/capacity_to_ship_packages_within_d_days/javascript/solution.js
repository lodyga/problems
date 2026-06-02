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
      const canShipInTime = (capacity) => {
         let currCapacity = 0;
         let transDays = 0;

         for (const weight of weights) {
            if (currCapacity >= weight) {
               currCapacity -= weight;
            } else {
               transDays += 1;
               currCapacity = capacity - weight;

               if (transDays > days) {
                  return false;
               }
            }
         }

         return true;
      }

      let left = Math.max(...weights);
      let right = weights.reduce((sum, val) => sum + val, 0);
      let res = right;

      while (left <= right) {
         const midCapacity = Math.floor((left + right) / 2);

         if (canShipInTime(midCapacity)) {
            res = midCapacity;
            right = midCapacity - 1;
         } else {
            left = midCapacity + 1;
         }
      }

      return res;
   }
}


const shipWithinDays = new Solution().shipWithinDays;
console.log(new Solution().shipWithinDays([1, 2, 3, 1, 1], 4) === 3)
console.log(new Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) === 15)
console.log(new Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3) === 6)
console.log(new Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) === 55)
console.log(new Solution().shipWithinDays([3, 3, 3, 3, 3, 3], 2) === 9)
