class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     A: iteration
    * @param {string} text
    * @return {number}
    */
   minOperations(text) {
      let diffA = 0;
      let diffB = 0;

      for (let index = 0; index < text.length; index++) {
         const a = index % 2 ? "0" : "1";
         const b = index % 2 ? "1" : "0";
         diffA += text[index] != a ? 1 : 0;
         diffB += text[index] != b ? 1 : 0;
      }

      return Math.min(diffA, diffB)
   };
}


const minOperations = new Solution().minOperations;
console.log(new Solution().minOperations('0100') === 1)
console.log(new Solution().minOperations('10') === 0)
console.log(new Solution().minOperations('1111') === 2)
