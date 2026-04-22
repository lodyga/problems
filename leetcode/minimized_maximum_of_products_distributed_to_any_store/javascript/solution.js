class Solution {
   /**
    * Time complexity: O(qlogm)
    *     q: quantities length
    *     m: max quantitity
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: binary search
    * @param {number} n
    * @param {number[]} quantities
    * @return {}
    */
   minimizedMaximum(n, quantities) {
      let low = 1;
      let high = Math.max(...quantities);
      let res = high;

      while (low <= high) {
         const mid = Math.floor((low + high) / 2);
         let countShops = 0;

         for (const q of quantities) {
            countShops += Math.ceil(q / mid);
            if (countShops > n) {
               break
            }
         }

         if (countShops > n) {
            low = mid + 1;
         } else {
            res = mid;
            high = mid - 1;
         }
      }

      return res
   };
}


const minimizedMaximum = new Solution().minimizedMaximum;
console.log(new Solution().minimizedMaximum(6, [11, 6]) === 3)
console.log(new Solution().minimizedMaximum(7, [15, 10, 10]) === 5)
console.log(new Solution().minimizedMaximum(1, [100000]) === 100000)
