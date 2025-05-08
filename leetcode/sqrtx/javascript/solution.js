class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: binary search
    * @param {number} square
    * @return {number}
    */
   mySqrt(square) {
      let left = 1;
      let right = square;

      while (left <= right) {
         const middle = (left + right) / 2 | 0;
         const currentSquare = middle ** 2;

         if (currentSquare === square)
            return middle
         else if (currentSquare > square)
            right = middle - 1;
         else
            left = middle + 1;
      }

      return right
   };
}


console.log(new Solution().mySqrt(4), 2)
console.log(new Solution().mySqrt(8), 2)