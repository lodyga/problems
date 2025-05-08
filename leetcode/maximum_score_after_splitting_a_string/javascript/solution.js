class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * @param {string} number
    * @return {number}
    */
   maxScore(number) {
      let prefixSum = 0;
      let postfixSum = number.split('').reduce((sum, number) => sum + Number(number), 0);
      let maxSum = 0;

      for (const digit of number.slice(0, -1)) {
         if (digit === '0') {
            prefixSum++;
         } else if (digit === '1') {
            postfixSum--;
         }
         maxSum = Math.max(maxSum, prefixSum + postfixSum);
      }

      return maxSum
   };
}
const maxScore = new Solution().maxScore;


console.log(new Solution().maxScore("011101"), 5)
console.log(new Solution().maxScore("00111"), 5)
console.log(new Solution().maxScore("1111"), 3)
console.log(new Solution().maxScore("00"), 1)