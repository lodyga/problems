class Solution {
   /**
    * Time complexity: O(nlogn)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     A: greedy, two pointers, sorting
    * @param {number[]} tokens
    * @param {number} power
    * @return {number}
    */
   bagOfTokensScore(tokens, power) {
      tokens.sort((a, b) => a - b);
      let score = 0;
      let maxScore = 0;
      let left = 0;
      let right = tokens.length - 1;

      while (left <= right) {
         if (power >= tokens[left]) {
            power -= tokens[left];
            score++;
            maxScore = Math.max(maxScore, score);
            left++;
         } else if (score) {
            power += tokens[right];
            score--;
            right--;
         } else {
            break
         }
      };

      return maxScore
   }
}


const bagOfTokensScore = new Solution().bagOfTokensScore;
console.log(new Solution().bagOfTokensScore([100], 50) === 0)
console.log(new Solution().bagOfTokensScore([200, 100], 150) === 1)
console.log(new Solution().bagOfTokensScore([100, 200, 300, 400], 200) === 2)
