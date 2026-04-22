class Solution {
   /**
    * Time complexity: O(logn)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {number} n
    * @return {number}
    */
   numberOfMatches(n) {
      let res = 0

      while (n > 1) {
         res += Math.floor(n / 2);
         n = Math.ceil(n / 2);
      }

      return res
   };
}


const numberOfMatches = new Solution().numberOfMatches
console.log(new Solution().numberOfMatches(7) === 6)
console.log(new Solution().numberOfMatches(14) === 13)
