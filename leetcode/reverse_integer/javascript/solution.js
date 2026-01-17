class Solution {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number} x
    * @return {number}
    */
   reverse(x) {
      const MIN = -(2 ** 31);  // -2_147_483_648
      const MAX = 2 ** 31 - 1;  // 2_147_483_647
      let res = 0;

      while (x) {
         const digit = x % 10;
         x = Math.trunc(x / 10);

         if (
            res > Math.floor(MAX / 10) ||
            res == Math.floor(MAX / 10) && digit > MAX % 10
         )
            return 0
         else if (
            res < Math.max(MIN / 10) ||
            res == Math.max(MIN / 10) && digit < MIN % 10
         )
            return 0

         res = (res * 10) + digit;
      }
      return res
   };
}


const reverse = new Solution().reverse;
console.log(new Solution().reverse(123) === 321)
console.log(new Solution().reverse(-123) === -321)
console.log(new Solution().reverse(120) === 21)
console.log(new Solution().reverse(-1563847412) === 0)
