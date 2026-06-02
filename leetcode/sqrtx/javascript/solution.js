class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    A: binary search
    * @param {number} X
    * @return {number}
    */
   mySqrt(X) {
      let left = 1;
      let right = X;
      let res = X;

      while (left <= right) {
         const mid = left + Math.floor((right - left) / 2);
         const square = mid**2;

         if (square === X) {
            return mid
         } else if (square < X) {
            res = mid;
            left = mid + 1;
         } else {
            right = mid - 1;
         }
      }

      return res;
   }
}


const mySqrt = new Solution().mySqrt;
console.log(new Solution().mySqrt(4) === 2)
console.log(new Solution().mySqrt(8) === 2)
