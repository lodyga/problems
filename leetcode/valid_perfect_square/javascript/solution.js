class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number} square
    * @return {boolean}
    */
   isPerfectSquare = function (square) {
      let left = 0;
      let right = square;

      while (left <= right) {
         const middle = (left + right) >> 1;
         const currentSquare = middle ** 2;

         if (currentSquare === square)
            return true
         else if (currentSquare > square) {
            right = middle - 1;
         } else
            left = middle + 1;
      }
      return false;
   };
}


console.log(new Solution().isPerfectSquare(16), true)
console.log(new Solution().isPerfectSquare(14), false)