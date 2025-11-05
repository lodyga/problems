class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {number} n
    * @return {boolean}
    */
   isPowerOfTwo(n) {
      if (n <= 0)
         return false

      while (n % 2 === 0)
         n >>= 1;

      return n === 1
   };

   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags: recursion
    * @param {number} n
    * @return {boolean}
    */
   isPowerOfTwo(n) {
      if (n <= 0)
         return false
      if (n % 2 === 0)
         return isPowerOfTwo(n >> 1)
      else
         return n === 1
   };

   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags: bit manipulation
    * @param {number} n
    * @return {boolean}
    */
   isPowerOfTwo(n) {
      return n > 0 && (n & (n - 1)) === 0
   };
}


const isPowerOfTwo = new Solution().isPowerOfTwo;
console.log(new Solution().isPowerOfTwo(1) === true)
console.log(new Solution().isPowerOfTwo(16) === true)
console.log(new Solution().isPowerOfTwo(3) === false)
console.log(new Solution().isPowerOfTwo(-4) === false)
console.log(new Solution().isPowerOfTwo(0) === false)
