class Solution {
   /**
    * Time complexity: O(nlogt)
    *     t: upper time limit
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: binary search
    * @param {number[]} ranks
    * @param {number} cars
    * @return {number}
    */
   repairCars(ranks, cars) {
      // Time to reapiar all cars.
      let left = 1;
      let right = Math.min(...ranks) * cars ** 2;
      let res = right;

      while (left <= right) {
         const mid = Math.floor((left + right) / 2);
         const repairedCars = ranks
            .map(rank => Math.floor((mid / rank) ** 0.5))
            .reduce((sum, num) => sum + num, 0);

         if (repairedCars < cars) {
            left = mid + 1;
         } else {
            res = mid;
            right = mid - 1;
         }
      }

      return res
   };

   /**
    * Time complexity: O(nlogt)
    *     t: upper time limit
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: binary search
    * @param {number[]} ranks
    * @param {number} cars
    * @return {number}
    */
   repairCars(ranks, cars) {
      const areCarsRepaired = (mid) => {
         let repairedCars = 0;

         for (const rank of ranks) {
            repairedCars += Math.floor((mid / rank) ** 0.5);
            if (repairedCars >= cars) return true
         }

         return false
      }

      // Time to reapiar all cars.
      let left = 1;
      let right = Math.min(...ranks) * cars ** 2;
      let res = right;

      while (left <= right) {
         const mid = Math.floor((left + right) / 2);

         if (areCarsRepaired(mid)) {
            res = mid;
            right = mid - 1;
         } else {
            left = mid + 1;
         }
      }

      return res
   };
}


const repairCars = new Solution().repairCars;
console.log(new Solution().repairCars([4, 2, 3, 1], 10) === 16)
console.log(new Solution().repairCars([5, 1, 8], 6) === 16)
