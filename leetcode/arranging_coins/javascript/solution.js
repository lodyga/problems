class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: binary search
    * @param {number} n
    * @return {number}
    */
   arrangeCoins(n) {
      let left = 1;
      let right = n;

      while (left <= right) {
         const mid = Math.floor((left + right) / 2);
         const coinCount = parseInt((1 + mid) * mid / 2);

         if (n === coinCount) {
            return mid
         } else if (n < coinCount) {
            right = mid - 1;
         } else {
            left = mid + 1;
         }
      }

      return right;
   }
}


const arrangeCoins = new Solution().arrangeCoins;
console.log(new Solution().arrangeCoins(1) === 1)
console.log(new Solution().arrangeCoins(2) === 1)
console.log(new Solution().arrangeCoins(3) === 2)
console.log(new Solution().arrangeCoins(4) === 2)
console.log(new Solution().arrangeCoins(5) === 2)
console.log(new Solution().arrangeCoins(6) === 3)
console.log(new Solution().arrangeCoins(8) === 3)
console.log(new Solution().arrangeCoins(1804289383) === 60070)
