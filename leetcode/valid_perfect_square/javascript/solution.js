class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: binary search
    * @param {number} square
    * @return {boolean}
    */
   isPerfectSquare(square) {
      let left = 0;
      let right = square;

      while (left <= right) {
         const mid = left + ((right - left) >> 1);
         const squared = mid ** 2;

         if (squared === square) {
            return true
         } else if (squared > square) {
            right = mid - 1;
         } else {
            left = mid + 1;
         }
      }

      return false;
   }
}


const isPerfectSquare = new Solution().isPerfectSquare;
console.log(new Solution().isPerfectSquare(16) === true)
console.log(new Solution().isPerfectSquare(14) === false)
