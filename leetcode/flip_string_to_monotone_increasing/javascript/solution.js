class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: greedy
    * @param {string} text
    * @return {number}
    */
   minFlipsMonoIncr(text) {
      let ones = 0;
      let flips = 0;
      for (const char of text)
         char == '1' ? ones += 1 : flips = Math.min(ones, flips + 1)
      return flips
   };
}


const minFlipsMonoIncr = new Solution().minFlipsMonoIncr;
console.log(new Solution().minFlipsMonoIncr('00') === 0)
console.log(new Solution().minFlipsMonoIncr('11') === 0)
console.log(new Solution().minFlipsMonoIncr('00110') === 1)
console.log(new Solution().minFlipsMonoIncr('010110') === 2)
console.log(new Solution().minFlipsMonoIncr('00011000') === 2)
console.log(new Solution().minFlipsMonoIncr('0101100011') === 3)
console.log(new Solution().minFlipsMonoIncr('10011111110010111011') === 5)
