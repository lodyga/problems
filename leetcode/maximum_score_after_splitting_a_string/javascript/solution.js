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
      let maxScr = 0;

      for (let index = 0; index < text.length - 1; index++) {
         text[index] === '0' ? score++ : score--;
         maxScr = Math.max(maxScr, score);
      }

      return maxScr
   };
}


const maxScore = new Solution().maxScore;
console.log(new Solution().maxScore('011101') === 5)
console.log(new Solution().maxScore('00111') === 5)
console.log(new Solution().maxScore('1111') === 3)
console.log(new Solution().maxScore('00') === 1)
