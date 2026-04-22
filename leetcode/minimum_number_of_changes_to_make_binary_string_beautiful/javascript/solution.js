class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: greedy, counting
    * @param {string} s
    * @return {number}
    */
   minChanges(s) {
      let res = 0

      for (let index = 0; index < s.length; index += 2) {
         if (s[index] !== s[index + 1]) {
            res += 1
         }
      }

      return res
   };
}


const minChanges = new Solution().minChanges;
console.log(new Solution().minChanges("10") === 1)
console.log(new Solution().minChanges("1001") === 2)
console.log(new Solution().minChanges("0000") === 0)
console.log(new Solution().minChanges("100100") === 2)
console.log(new Solution().minChanges("100111") === 2)
