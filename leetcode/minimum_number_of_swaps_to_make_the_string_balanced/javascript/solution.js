class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *     DS: string
    *     A: greedy
    * @param {string} s
    * @return {number}
    */
   minSwaps(s) {
      let opened = 0;
      let swaps = 0;

      for (const char of s) {
         if (char == '[') {
            opened++;
         } else if (opened) {  // char == ']'
            opened--;
         } else {
            opened++;
            swaps++;
         }
      }

      return swaps
   };
}


const minSwaps = new Solution().minSwaps;
console.log(new Solution().minSwaps('[]') === 0)
console.log(new Solution().minSwaps('][][') === 1)
console.log(new Solution().minSwaps(']]][[[') === 2)
console.log(new Solution().minSwaps('][[]][][[][]') === 1)
console.log(new Solution().minSwaps('[[[]]]][][]][[]]][[[') === 2)
