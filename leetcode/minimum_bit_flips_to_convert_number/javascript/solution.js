class Solution {
   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {number} start
    * @param {number} goal
    * @return {number}
    */
   minBitFlips(start, goal) {
      let n = start ^ goal;
      let res = 0;

      while (n) {
         res += n & 1;
         n >>= 1;
      }

      return res
   };

   /**
    * Time complexity: O(1)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: bit manipulation
    * @param {number} start
    * @param {number} goal
    * @return {number}
    */
   minBitFlips(start, goal) {
      let n = start ^ goal;
      let res = 0;

      while (n) {
         res++;
         n = n & (n - 1);
      }

      return res
   };
}


const minBitFlips = new Solution().minBitFlips;
console.log(new Solution().minBitFlips(10, 7) === 3)
console.log(new Solution().minBitFlips(3, 4) === 3)
