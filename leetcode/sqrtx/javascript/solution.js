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
         const middle = left + ((right - left) >> 1);
         const currentSquare = middle * middle;

         if (currentSquare === X) {
            return middle
         }
         else if (currentSquare < X) {
            res = middle;
            left = middle + 1;
         }
         else {
            right = middle - 1;
         }
      }
      return res
   };
}


const mySqrt = new Solution().mySqrt;
console.log(new Solution().mySqrt(4) === 2)
console.log(new Solution().mySqrt(8) === 2)
