class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags:
    *    DS: string
    *     A: iteration
    * @param {string} text
    * @return {number}
    */
   maxScore(text) {
      let score = text.split('').filter(bin => bin === '1').length;
      let res = 0;

      for (let idx = 0; idx < text.length - 1; idx++) {
         const chr = text[idx];
         text[idx] === '0' ? score++ : score--;
         res = Math.max(res, score);
      }

      return res;
   }
}


const maxScore = new Solution().maxScore;
console.log(new Solution().maxScore('011101') === 5)
console.log(new Solution().maxScore('00111') === 5)
console.log(new Solution().maxScore('1111') === 3)
console.log(new Solution().maxScore('00') === 1)
