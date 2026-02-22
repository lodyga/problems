class Solution {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     bit manipulation, iteration
    * @param {number} n
    * @return {boolean}
    */
   isPowerOfTwo(n) {
      return n > 0 && (n & (n - 1)) === 0
   };

   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     bit manipulation, iteration
    * @param {number} n
    * @return {boolean}
    */
   isPowerOfTwo(n) {
      if (n <= 0) {
         return false
      }

      while (n !== 1) {
         if (n & 1) {
            return false
         }
         n >>= 1;
      }

      return true
   };

   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     iteration
    * @param {number} n
    * @return {boolean}
    */
   isPowerOfTwo(n) {
      if (n <= 0)
         return false

      while (n % 2 === 0)
         n = Math.floor(n / 2);

      return n === 1
   };

   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     recursion
    * @param {number} n
    * @return {boolean}
    */
   isPowerOfTwo(n) {
      if (n <= 0) {
         return false
      } else if (n % 2) {
         return n === 1
      } else {
         return isPowerOfTwo(Math.floor(n / 2))
      }
   };
}


const isPowerOfTwo = new Solution().isPowerOfTwo;
console.log(new Solution().isPowerOfTwo(1) === true)
console.log(new Solution().isPowerOfTwo(16) === true)
console.log(new Solution().isPowerOfTwo(3) === false)
console.log(new Solution().isPowerOfTwo(-4) === false)
console.log(new Solution().isPowerOfTwo(0) === false)
