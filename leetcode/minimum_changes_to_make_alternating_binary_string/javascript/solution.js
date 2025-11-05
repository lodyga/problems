class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: iteration
    * @param {string} text
    * @return {number}
    */
   minOperations(text) {
      let zero = 0  // target 0101...
      let one = 0  // target 1010...

      for (let index = 0; index < text.length; index++) {
         const char = text[index];
         if (index % 2) {
            // 0101...
            if (char === '0')
               zero++;
            // 1010...
            else
               one++;
         }
         else {
            // 0101...
            if (char === '1')
               zero++;
            // 1010...
            else
               one++;
         }
      }
      return Math.min(zero, one)
   };
}


const minOperations = new Solution().minOperations;
console.log(new Solution().minOperations('0100') === 1)
console.log(new Solution().minOperations('10') === 0)
console.log(new Solution().minOperations('1111') === 2)
